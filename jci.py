import clang.cindex
import argparse


def parse_file(filename):

    # Create an index and parse the given file to get the translation unit
    index = clang.cindex.Index.create()
    translation_unit = index.parse(filename)

    def traverse(cursor):

        # Check if the cursor is a function call expression and if it is in the given file
        if (
            cursor.kind == clang.cindex.CursorKind.CALL_EXPR
            and cursor.location.file.name == filename
        ):
            pass
        
        # Recursively traverse children of the current cursor
        for child in cursor.get_children():
            traverse(child)

    # Start traversing from the root cursor of the translation unit
    traverse(translation_unit.cursor)
    return True