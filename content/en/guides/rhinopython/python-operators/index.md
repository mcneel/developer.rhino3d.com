+++
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide is an overview of Python operators."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Python Operators"
type = "guides"
weight = 10
override_last_modified = "2020-03-06T10:19:02Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Overview

Python has a full range of operators, including arithmetic operators, comparison operators, concatenation operators, and logical operators.

## Operator Precedence

When several operations occur in an expression, each part is evaluated and resolved in a predetermined order called operator precedence.  You can use parentheses to override the order of precedence and force some parts of an expression to be evaluated before others.  Operations within parentheses are always performed before those outside.  Within parentheses, however, standard operator precedence is maintained.

When expressions contain operators from more than one category, arithmetic operators are evaluated first, comparison operators are evaluated next, and logical operators are evaluated last.  Comparison operators all have equal precedence; that is, they are evaluated in the left-to-right order in which they appear.  Arithmetic and logical operators are evaluated in the following order of precedence.

### Arithmetic

| Description |      | Symbol |
| :---------- | ---- | -----: |
 | Exponentiation |    | `**` |
 | Unary negation |    | `-` |
 | Multiplication |    | `*` |
 | Division |    | `/` |
 | Integer Division |    | `//` |
 | Modulus arithmetic |    | `%` |
 | Addition |    | `+` |
 | Subtraction |    | `-` |
 | String concatenation |    | `+` |


### Comparison

| Description |      | Symbol |
| :---------- | ---- | -----: |
 | Less than |    | `<` |
 | Greater than |    | `>` |
 | Less than or equal to |    | `<=` |
 | Greater than or equal to |    | `>=` |
 | Equality |    | `==` |
 | Inequality |    | `!=` |
 | Object equivalence |    | `is` |


### Logical

| Description |      | Symbol |
| :---------- | ---- | -----: |
 | Logical negation |   | `not` |
 | Logical conjunction |    | `and` |
 | Logical disjunction |    | `or` |


## Considerations

When multiplication and division occur together in an expression, each operation is evaluated as it occurs from left to right.  Likewise, when addition and subtraction occur together in an expression, each operation is evaluated in order of appearance from left to right.

The string concatenation (`+`) operator is not an arithmetic operator, but in precedence it falls after all arithmetic operators and before all comparison operators.  The `is` operator is an object reference comparison operator.  It does not compare objects or their values; it checks only to determine if two object references refer to the same object.

## Related Topics

- [What are VBScript and RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript)
