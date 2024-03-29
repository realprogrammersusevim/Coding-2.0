Perl Tengwar Transcriber  
version 1.2, June 2006  
Author: Ignacio Fernández Galván (Jellby): jellby@yahoo.com  
Homepage: djelibeibi.unex.es/tengwar  


## INTRODUCTION

Perl Tengwar Transcriber (ptt) is a Perl script designed for converting
texts written with the roman alphabet into tengwar (and vice-versa).
Unlike other similar tools, ptt does not rely on tengwar fonts following
Dan Smith's encoding. Some modes are provided for converting into the
TengwarScript LaTeX package format (available in the homepage), but it
is straightforward to convert this to any other format. A mode file for
conversion into Dan Smith's encoding is also provided.


## INSTALLATION AND REQUISITES

Being a Perl script, ptt needs a working Perl instalation. This should
be no problem for Linux users. Windows, MacOS and other OS users may
have to download and install Perl, I don't know.

In order to transcribe texts, an appropriate mode file for the language
used is required too. Quenya and Spanish modes are included in this
package, other modes may be available soon, or maybe not... If you write
a mode file yourself, please let me know so I can add it to the package.


## USAGE

In a linux system, just make sure that the ptt.pl file has execution
permisions and that the path in its first line is correct for your
system. Then run:

``./ptt.pl``

You'll get a short usage notice. To transcribe a text in roman to
tengwar use the following command.

``./ptt.pl [options] mode-file [text-file] [output-file]``

where mode-file is the mode file to use, text-file is the file with the
text you want to transcribe and output-file is the file where you want
the output to be written. If you omit output-file, the standard output
will be used. If you omit both input-file and output-file, you'll be
asked to write the text, which will be read from the standard input, and
the output will be sent to the standard output.

The options must be preceded by a hyphen (-) and all in the same "word",
i.e., write "-drq" and not "-d -r -q" A description for the different
options follows:

``-d``
  When transcribing numbers (if the mode file has number patterns),
output tengwar numbers as decimal (base 10). Default is duodecimal (base
12) numbers.

``-h``
``-?``
  Writes the usage notice and exits.
  
``-m``
  Don't make any transcription, just read and check the mode file.

``-n``
  When transcribing numbers (if the mode file has number patterns),
output tengwar numbers in left-to-right order (rightmost digit is the
least significant). Default is right-to-left order.

``-o``
  Use standard input as input-file, but still send the output to a real
file and not to the standard output. If you use this option, you specify
an output-file but no input-file. This is useful for pipes (see below:
Conversion to Dan Smith's Encoding).

``-p``
  Modify the way the transcription is performed by enabling or disabling
transcription mode options (defined in the mode-file) The options are
given in a separate "word" before the mode-file (see below:
Transcription Mode Options).

``-q``
  Quiet mode. Don't print any message to the output, just do the
transcription.

``-r``
  Do a tengwar to roman transcription instead of roman to tengwar. When
doing the reverse transcription, the number format will be recognized,
unless it is decimal left-to-right (because decimal numbers don't have a
least significant mark in tengwar), in which case you should specify the
-n option too (see above)

``-v``
``-vv``
  Give more info about the mode file being used. -v shows the number of
patterns in the mode file, whether it is case sensitive and whether it
includes number patterns. `-vv` shows also all the patterns in the mode
file.

### Conversion to Dan Smith's Encoding

Although the primary goal of ptt is to generate input for the
TengwarScript LaTeX package, it can also be used for generating text
suitable for fonts using the "standard" Dan Smith encoding (or any other
encoding, actually). For this task, instead of providing new mode files
for every language, it is better to have a single mode file that
converts the "TeX" output into "Dan Smith" option. This mode file is
called ts2ds.ptm, and I hope it's easy enough to use.

You can first transcribe into the TengwarScript package format, and then
convert it:

  ``./ptt.pl mymode.ptm story.txt story.tex``
  ``./ptt.pl ts2ds.ptm story.tex story.tng``

or you can use a pipe:

``./ptt.pl -q mymode.ptm story.txt | ./ptt.pl -o ts2ds.ptm story.tng``

here, the first ``./ptt.pl`` uses the ``-q`` option so that no messages are
transferred the the second command, while the second ``./ptt.pl`` uses the
``-o`` option to get the input from the first one and still being able to
provide an output file.

Similarly, to convert a text written for Dan Smith's encoding into the
tengwar package for LaTeX format, use:

  ``./ptt.pl -r ts2ds.ptm story.tng story.tex``

### Transcription Mode Options

  A mode file can contain itself different options which affect the
output of the transcription. For instance, an option can control whether
a final "s" is transcribed as a full tengwa or as an s-hook, another
option can control the way in which dipthongs are transcribed; the mode
file has to be built to support these options. Each option is a
two-state toggle, it can be either enabled or disabled. To see which
specific options a mode file is designed to support, you can run
"./ptt.pl -mv mode-file", if the mode file has built-in options
something like this will appear on the screen:

Mode options:
| (def) | (sel) | add | description |
| ----- | ----- | --- | ----------- |
| +1 | * | (1) | Vowels as tehtar |
| +2 | * | (2) | Dipthongs and tripthongs |
| +3 | * | (4) | Double tehtar for accents |
| -4 |   | (8) | Vertical bars for accents |
| +5 | * | (16) | Tilde for preceding nasal |
| +6 | * | (32) | Hook for final s |
| +7 | * | (64) | Use silme nuquerna |
| -8 |   | (128) | Basic pronunciation mode |
| -9 |   | (256) | Roman pronunuciation |

Default: 119

  This particular mode file supports 9 options. The first column
displays the number of each option and its default state: "+2" means
option 2 is enabled by default (dipthongs will be transcribed in a
special way), "-9" means option 9 is disabled by default (tengwar
symbols, not roman, will be used for punctuation). The second column
shows which options are enabled at the moment, since no option change
has been given in the command line, the enabled options are just the
default ones, but they can be altered with the -p option for ptt. The
third column contains the number you should add to specify the options
in binary format (see below). The last column is a short description of
what happens when the option is enabled. The line saying "Default: 119"
gives the binary value of the default options, it can be obtained by
adding the values in the third column for options enabled by default
(1+2+4+16+32+64 = 119).

  If you want to change the default transcription options, you can do so
by passing the -p option to ptt. After this option, and before the
mode-file, you must specify a "word" containing the set of transcription
options you want to enable or disable, this can be done in two ways:

1) Individual options can be enabled or disabled by writing their
numbers preceded by + or -. Several options can be given in this way,
options which value is not given here will take their default values.
For example, "+4-6" enables option 4 and disables option 6, other
options are set to the default.

2) The state of all options can be set at the same time with a single
number, which is interpreted as a binary chain of states. You can obtain
this number by adding the values in the third column only for the
options you want enabled, the rest will be disabled. For example, "47"
will enable only options 1, 2, 3, 4, and 6, since 1+2+4+8+32 = 47.

Usually, transcription mode options affect only the roman to tengwar
transcription, while the tengwar to roman transcription is more
constant, so you can often safely leave out the -p option when doing a
reverse transcription (with the -r option). However, some options can be
more drastic and really change the equivalence of the tengwar, so in
some cases you should also specify the correct transcription mode
options when transcribing back to roman.


## TEST

A simple test is included in the directory "test". You'll find there two
files: "frases.txt", which contains two pangrams and numbers in Spanish,
and "frases.tex", which is an input file for LaTeX (it requires the
TengwarScript package). To run the test:

1. Transcribe to tengwar the txt file. Assuming you run it from the test
   directory: `../ptt.pl ../es.ptm frases.txt frases.tng`  Now you'll see the LaTeX (TengwarScript) commands in frases.tng.

2. Compile the frases.tex file, preferably with pdflatex: `pdflatex frases.tex`

If everything went fine, you'll now have a pdf file with the original
text and the tengwar transcription. You can try passing some options to
ptt and the mode file, for instance:
  "../ptt.pl -dp -1+9 ../es.ptm frases.txt frases.tng"
and recompiling frases.tex. You'll get decimal numbers, roman
punctuation, and vowels as individual tengwar.


## MODE FILES

ptt does not use the mode files used by other programs like Tengwar
Scribe or YaTT; this may be a limitation, but it is so because its own
format is, I hope, more powerful and easier to edit. The modes for ptt
have the extension .ptm (Perl Tengwar Mode). What follows is a
description of this format.

### Header

The mode file starts with a header of four lines with this format:

  1st line: literal "#<Perl-TMF>", a tab, arbitrary text
  2nd line: literal "#r2t", a tab, number of roman-to-tengwar patterns
  3rd line: literal "#t2r", a tab, number of tengwar-to-roman patterns
  4th line: literal "#cs", a tab, 0 or 1

The arbitrary text in the first line will be shown when using this mode.
The number of roman-to-tengwar and tengwar-to-roman patterns doesn't
have to match the number of actual patterns in the file, but if it
doesn't a warning will be issued. The fourth line should have a 1 if the
mode is case-sensitive and 0 otherwise; case-sensitivity affects only
roman-to-tengwar patterns.

A mode file can include options which modify the way the transcription
is made, for instance, an option could tell whether a final "s" is
transcribed as a tengwa or as an s-hook. If a mode file has options, the
5th line should contain:

  Literal "#OPTIONS:"

and then the different options should follow. Each option is given in a
line with the format:

  Literal "#", num, an optional "*", a tab, text1

where num is the number of each option and text1 is a description for
it. If the optional * is present, the option will be enabled by default.

### Text patterns

The patterns description starts with the following line:

  Literal "#pat", a tab, "conv", a tab, "next", a tab, "prev"

After that, every line is a roman-to-tengwar pattern, until the
following line is found:

  Literal "#==="

Then every line is a tengwar-to-roman pattern, until a line like the
above is found.

There is one exception, every line starting with a tab is considered as
a comment and is not counted, this allows to insert comments and to
temporarily disable patterns.

The structure of each pattern is the following:

  text1, a tab, text2, a tab, regexp1, a tab, regexp2

where text1 and text2 are just text fragments, and regexp1 and regexp2
are treated as Perl regular expresions, that means that, among other
things, character classes can be used and some characters must be
escaped with a backslash. See "man perlrequick" for a quick reference.

When transcribing, *if* "text1" is found in the input text *and if*
regexp1 matches just after (and not including) it *and if* regexp2
matches just before (and not including) it, *then* text2 is written to
the output. regexp1 and regexp2 can be empty, and then they always
match; text2 can be empty, and nothing is written to the output; but the
tabs must always be present! The patterns are checked in order, so the
ordering is important; in general, place more restrictive and longer
patterns higher in the mode file.

Additionally, each text pattern can be followed, in the same line, by an
options fragment which has the format:

  a tab, (+ or -, num) any number of times.

where num is the number of an option. If the sign is +, the pattern will
be active only if the option is enabled; if the sign is -, the pattern
will be active only if the option is disabled. When several options
(with their signs) are given, the pattern will be active only when *all*
conditions are satisfied, i.e., a pattern with the options "+2-5" will
only be active when option #2 is enabled and option #5 is disabled, the
state of other options does not matter. If a pattern is not active, it's
simply ignored.

### Number patters

If the mode includes number patterns, the next line after the last
"#===" will be:

  Literal "#digit", a tab, "dec", a tab, "duodec", a tab, "least"

And then there must be exactly 12 lines with the following format:

  num, a tab, text1, a tab, text2, a tab, text3

where num is a number in order from 00 to 11, and text1, text2 and text3
are the corresponding transcriptions in tengwar. text1 will be used for
decimal numbers, text2 for duodecimal numbers, and text3 for the least
significant digits in duodecimal numbers. text1 can be empty for 10 and
11.


## BUGS, LIMITATIONS, PROBLEMS...

As in any program, some bugs may be present, though I'm not aware of
any... yet.

As for limitations, the main one is the lack of mode files. Given some
time and help I may be able to write some additional mode files for
Sindarin, English, and more. Another possible limitation is that ptt has
only been tested with iso-8859-1(5) locale and files, I'm not sure about
how it will work with other encodings like utf8.

Also, no special effort has been taken to optimise the code, so it may
be too slow for long texts, but I believe it's OK for a couple of pages.

If you find some other problem, please let me know, and better yet if
you fix it!


## CHANGELOG

17/06/2006: Version 1.2.

17/04/2006: Optimized a bit the pattern search by sorting and indexing.

16/04/2006: Added the possibility of transcription mode options, and modified the Spanish and Quenya modes to use them.

10/12/2005: Added Quenya mode.

19/11/2005: First release 1.0.


## LICENSE

This program is distributed under the GNU Public License (GPL), see the
included file COPYING.
