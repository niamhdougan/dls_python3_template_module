import os
import sys
from argparse import ArgumentParser


def maybe_warn_snippet(path, *snippets):
    # type: (str, str) -> None
    path = os.path.abspath(path)
    if os.path.exists(path):
        with open(path) as f:
            dest_text = f.read()
    else:
        dest_text = ""
    if any(snippet not in dest_text for snippet in snippets):
        print(
            """Please add the following snippet to %s:
--------------------------------------------------------------------------------
%s
--------------------------------------------------------------------------------
"""
            % (path, "\n".join(snippets))
        )


def main():
    from versiongit import __version__

    parser = ArgumentParser(
        description="Command line tool adding versiongit to python module"
    )
    parser.add_argument(
        "--version", action="store_true", help="Print the current version of versiongit"
    )
    parser.add_argument(
        "dir", nargs="?", help="The directory to add _version_git.py to"
    )
    args = parser.parse_args()
    if args.version:
        print(__version__)
    else:
        assert args.dir and os.path.isdir(args.dir), (
            "Expected a python package directory, got %r" % args.dir
        )
        versiongit_path = os.path.dirname(os.path.abspath(__file__))
        # Write _version_git.py with descriptive header
        with open(os.path.join(versiongit_path, "_version_git.py")) as f:
            lines = f.readlines()
        header = (
            """# Compute a version number from a git repo or archive

# This file is released into the public domain. Generated by:
# versiongit-%s (https://github.com/dls-controls/versiongit)
"""
            % __version__
        )
        # Make sure when running from git archive, the format strings are put
        # back in
        for i, line in enumerate(lines):
            split = line.split(" = ")
            if split[0] == "GIT_ARCHIVE_REF_NAMES":
                split[1] = '"$Format:%D$"\n'
            elif split[0] == "GIT_ARCHIVE_HASH":
                split[1] = '"$Format:%h$"\n'
            else:
                continue
            lines[i] = " = ".join(split)
        with open(os.path.join(args.dir, "_version_git.py"), "w") as f:
            f.write(header)
            f.writelines(lines)
        print("Added %s\n" % os.path.join(args.dir, "_version_git.py"))
        # Make sure __init__.py lines are in
        maybe_warn_snippet(
            os.path.join(args.dir, "__init__.py"),
            """try:
    # In a release there will be a static version file written by setup.py
    from ._version_static import __version__  # type: ignore
except ImportError:
    # Otherwise get the release number from git describe
    from ._version_git import __version__"""
        )
        # Make sure .gitattribute lines are in
        maybe_warn_snippet(
            os.path.join(args.dir, "..", ".gitattributes"),
            "*/_version_git.py export-subst",
        )
        # Make sure the setup.py lines are in
        maybe_warn_snippet(
            os.path.join(args.dir, "..", "setup.py"),
            """# Place the directory containing _version_git on the path
for path, _, filenames in os.walk(os.path.dirname(os.path.abspath(__file__))):
    if "_version_git.py" in filenames:
        sys.path.append(path)
        break

from _version_git import get_cmdclass, __version__
""",
            "setup(",
            "    cmdclass=get_cmdclass(),",
            "    version=__version__",
            ")",
        )


if __name__ == "__main__":
    sys.path.insert(1, os.path.join(os.path.dirname(__file__), ".."))
    main()
