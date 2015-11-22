#! /usr/bin/env python

import os
from xml.etree.ElementTree import Element, SubElement, tostring

LIBRARY_JAR_ROOT = os.path.join('bazel-genfiles', 'external')

def main():
    print('Generating .classpath file ...')
    with open('.classpath', 'w') as file:
        file.write(generate_classpath_contents())

    print('Generating .project file ...')
    # TODO(dino): Actually generate .project.

    print('Done')

def generate_classpath_contents():
    jar_paths = discover_jars(LIBRARY_JAR_ROOT)
    jar_entries = '\n'.join([CLASSPATH_INDENT + jar_entry(p) for p in jar_paths])
    return CLASSPATH_TEMPLATE % { 'jar_entries': jar_entries }

def jar_entry(jar_path):
    return JAR_CLASSPATH_ENTRY_TEMPLATE % {'path': jar_path}

def discover_jars(root):
    jar_paths = []
    for root, _, files in os.walk(LIBRARY_JAR_ROOT):
        for file in files:
            if os.path.splitext(file)[1] == '.jar':
                jar_paths.append(os.path.abspath(os.path.join(root, file)))
    return jar_paths

CLASSPATH_TEMPLATE = """
<?xml version="1.0" encoding="UTF-8"?>
<classpath>
        <classpathentry kind="src" path="src/main/java"/>
        <classpathentry kind="src" path="src/test/java"/>
        <classpathentry kind="con" path="org.eclipse.jdt.launching.JRE_CONTAINER"/>
%(jar_entries)s
</classpath>
"""

CLASSPATH_INDENT = """        """

JAR_CLASSPATH_ENTRY_TEMPLATE = '<classpathentry kind="lib" path="%(path)s"/>'

if __name__ == '__main__':
    main()
