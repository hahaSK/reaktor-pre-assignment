#!/usr/bin/python

"""
    Author: Ing. Juraj Lahvička
    2020
"""

import re
import sys

import html_handler

from Package import PackageCls


def add_dependencies(pack, depend_str):
    """Parses dependencies into package instance dependency list"""
    depends = depend_str.split(',')
    for depend in depends:
        if depend.__contains__('|'):
            depends.remove(depend)
            depends += depend.split('|')

    for depend in depends:
        # Remove version
        depend = re.sub(r'\(.*\)', '', depend)
        depend = depend.strip()
        if depend not in pack.DependsList:
            pack.DependsList.append(depend)


def parse_file(path):
    """Function parses the packages file into list of PackageCls"""
    try:
        packages = list()
        with open(path, encoding="utf-8") as file:
            packages_file = re.split('^$', "".join(file.readlines()), flags=re.MULTILINE)

        # The last item is empty, need to remove it
        packages_file = packages_file[:-1]
        for package in packages_file:
            name = re.findall('(?<=Package: )(.*)', package, flags=re.MULTILINE)[0]

            description_header = re.findall('(?<=Description: )(.*)', package, flags=re.MULTILINE)
            description_body = re.findall('(?<=^ )(.*)', package, flags=re.MULTILINE)
            description = description_header + description_body
            description = (" ".join(description)).replace(' . ', '\n')

            pack = PackageCls(name, description)
            depend = re.findall('(?<=Depends: )(.*)', package, flags=re.MULTILINE)
            if len(depend) > 0:
                add_dependencies(pack, depend[0])

            packages.append(pack)

        return packages

    except FileExistsError:
        print(f"File not found. Path: {path}")
        sys.exit(1)


def get_reverse_dependencies(packages):
    """Adds reverse dependencies"""
    for package in packages:
        for other_package in packages:
            if package.Name in other_package.DependsList:
                package.ReverseDependencies.append(other_package.Name)
        # Removes duplicates
        set(package.ReverseDependencies)


def main():
    if len(sys.argv) != 2:
        raise Exception("Unsupported arguments! Expected path to status file.")

    path = sys.argv[1]
    packages = parse_file(path)
    get_reverse_dependencies(packages)
    html_handler.create_html(packages)


if __name__ == "__main__":
    # execute only if run as a script
    main()
