escape_sequence = """
escape
\\ Backslash(\)
\' Single quote (')
\" Double quote (")
\a ASCII bell (BEL)
\b ASCII backspace (BS)
\f ASCII formfeed (FF)
\n ASCII linefeed (LF)
\n{name} Character named name in unicode database (unicode only)
\r ASCII carriage return
\t ASCII horizontal tab
\uxxxx Character with 16 bit hex value xxxx (unicode only)
\Uxxxxxxxx Character with 32 bit hex value xxxxxxxx (unicode only)
\v ASCII vertical tab (VT)
\ooo Character with octal value 00
\xhh Character with hex value hh
"""

print escape_sequence