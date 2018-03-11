.. This is a comment
..
   _so: is this!
..
   [and] this!
..
   this:: too!
..
   |even| this:: !

################################
reStructuredText Quick Reference
################################

Basic Formatting
================

**bold**

*italics*

``this is a code sample``

.. code-block:: javascript

   const o = ()=> console.log("this is also a code block")

usingmarkup\ **in**\ strings\ :superscript:`thisissuperscript`\ :subscript:`thisissubscript`

author name, :title-reference:`this is a book title` (NY: New York University Press, 2018)

Headers
=======

Section headers are created by underlining (and optionally overlining) the section title with a punctuation character, at least as long as the text:

.. code-block:: rst

   =================
   This is a heading
   =================

The structure is determined from the succession of headings — there is no way to explicitly determine header levels. Python documentation suggests the following conventions:

* ``#`` with overline, for parts
* ``*`` with overline, for chapters
* ``=``, for sections
* ``-``, for subsections
* ``^``, for subsubsections
* ``"``, for paragraphs

Lists
=====

List

* Item 1
* Item 2
    * Nested item 1
    * Nested item 2
* Item 3

List

1. Item 1
2. Item 2
    1. Nested item 1
    2. Nested item 2
3. Item 3

List

#. Item 1
#. Item 2
    #. Nested item 1
    #. Nested item 2

Hyperlinks
==========

This is how to write hyperlinks_. Hyperlink targets can accept `spaces in names`_ by enclosing the hyperlink text in backticks.

.. _hyperlinks: http://example.com
.. _spaces in names: http://example.com

Internal hyperlinks have no link specified in the directive. Instead, internal hyperlink targets can be specified by writing the hyperlink directive above the target element. For example, this hyperlink goes here_.

.. _here:

.. topic:: Hyperlink target
   
   This is the hyperlink target.

Admonitions
===========


.. admonition:: custom caption

   This is a custom admonition


.. caution::

   Caution!
   
   Write more than one line

List of admonitions available:

* admonition
* attention
* caution
* danger
* error
* hint
* important
* note
* tip
* warning

Images
======

The ``.. image:: <path>`` directive allows you to specify ``:height: <h>`` and ``:width: <w>`` options. Also can apply the ``:scale: <percent>`` option. Use the ``:target: <url>`` option to turn the image into a clickable link.

.. image:: /_static/IMG_0049.*
   :width: 100%
   :target: http://example.com

The ``.. figure:: <path>`` directive inserts an image, and allows caption content. Accepts either a ``:scale: <percent>`` or a ``:figwidth: <w>`` option. ``:figclass: <class>`` option allows you to assign the figure a class.


.. figure:: /_static/IMG_0049.*
   :scale: 50 %
   :alt: map to buried treasure
   :figwidth: 100%
   :figclass: .asdf

   This is the caption of the figure (a simple paragraph).

   The legend consists of all elements after the caption.  In this
   case, the legend consists of this paragraph and the following
   table:

   +---------------------------+-----------------------+
   | Symbol                    | Meaning               |
   +===========================+=======================+
   | ``.. image:: tent.png``   | Campground            |
   +---------------------------+-----------------------+
   | ``.. image:: waves.png``  | Lake                  |
   +---------------------------+-----------------------+
   | ``.. image:: peak.png``   | Mountain              |
   +---------------------------+-----------------------+

Body elements
=============

.. sidebar:: Sidebar title
   :subtitle: Optional subtitle
   :class: sidebar_class
   :name: this_sidebar

   This is a sidebar. You can use the ``:subtitle: <text>`` and the ``:class: <class>`` option. The ``:name: <name>`` option assigns the sidebar an ID.

   Place the sidebar at the top of the text paragraph or element that you want the sidebar to sidebar.

.. epigraph::

   No matter where you go, there you are.

   -- Buckaroo Banzai

Lorem dim sum Rice noodle roll deep fried crab claw soup dumpling cold chicken claw xo spicy rice noodle roll honey glazed BBQ pork soy sauce chicken roast duck. Jin deui Chicken feet Potstickers stir fried radish cake Steamed Bun with Butter Cream hot raw fish slices porridge traditional steamed glutinous rice.

Deep fried garlicky fish ball chee cheong fun with barbecued pork steamed radish cake steamed bun with premium lotus paste cabbage roll paekuat.

Cha siu sou Cheong fan pan fried bitter melon beef dumpling mango pudding coconut milk pudding black sesame soft ball deep fried bean curd skin rolls.

Stir fried radish cake Steamed Bun with Butter Cream hot raw fish slices porridge traditional steamed glutinous rice with zhu hao sauce crispy yam puff crispy dragon roll honeydew puree with sago.

Jiu cai bau Zhaliang Pei guen Lo baak gou Taro cake. Dried scallop and leek puff deep fried seaweed roll BBQ pork puff Pan friend pork dumpling Pot sticker water chestnut cake bitter melon beef dumplings turnip cake leek dumplings deep fried taro turnover.

.. topic:: This is a topic
   :class: classname
   :name: asdf

   A topic is like a block quote with a title, or a self-contained section with no subsections. Use the "topic" directive to indicate a self-contained idea that is separate from the flow of the document. Topics may occur anywhere a section or transition may occur. Body elements and topics may not contain nested topics.

   The directive's sole argument is interpreted as the topic title; the next line must be blank. All subsequent lines make up the topic body, interpreted as body elements.

Writing References
==================

Footnotes
---------

Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_. Use a rubric\ [#f3]_ to designate an informal heading.

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.
.. [#f3] rubric n. 1. a title, heading, or the like, in a manuscript, book, statute, etc., written or printed in red or otherwise distinguished from the rest of the text. An informal heading that doesn't correspond with the document structure.

Citations
---------

Lorem ipsum\ [Ref]_ dolor sit amet.

\[…\]

.. [Ref] Book or article reference, URL or whatever.

Variables
=========

Variables are defined using the following syntax:

.. code-block:: rst

   .. |<variable_name>| <directive>::<arg>
      [:dir_options:]

      [<dir_content>]


Simple text variables use the ``.. replace:: <text>`` directive.

This is a variable: |varname|

.. |varname| replace:: variable name

An example of a more complex text replacement:

.. code-block:: rst
   
   But still, that's nothing compared to a name like |j2ee-cas|__.

   .. |j2ee-cas| replace::
      the Java `TM`:superscript: 2 Platform, Enterprise Edition Client
      Access Services
   __ http://developer.java.sun.com/developer/earlyAccess/
      j2eecas/

Gives us:

But still, that's nothing compared to a name like
|j2ee-cas|__.

.. |j2ee-cas| replace::
   the Java `TM`:superscript: 2 Platform, Enterprise Edition Client
   Access Services
__ http://developer.java.sun.com/developer/earlyAccess/
   j2eecas/

Variables can also use the ``.. images::`` directive. For example, |sub_image|.

.. |sub_image| image:: /_static/IMG_0049.*
   :width: 100px

Use variables to insert unicode characters. For example, ``.. |copy| unicode:: 0xA9 .. copyright sign`` inserts |copy|.

.. |copy| unicode:: 0xA9 .. copyright sign

HTML metadata
=============

Adding metadata to HTML pages helps SEO.

An example of a ``.. meta::`` directive:

.. code-block:: rst
   
   .. meta::
      :description lang=en: The reStructuredText plaintext markup language.
      :description lang=de: Ich spreche nein Deutsche.
      :keywords: plaintext, markup language
      :http-equiv=Content-Type: text/html; charset=ISO-8859-1