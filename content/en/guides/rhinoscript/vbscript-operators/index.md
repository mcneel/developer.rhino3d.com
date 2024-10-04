+++
aliases = ["/en/5/guides/rhinoscript/vbscript-operators/", "/en/6/guides/rhinoscript/vbscript-operators/", "/en/7/guides/rhinoscript/vbscript-operators/", "/wip/guides/rhinoscript/vbscript-operators/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide is an overview of VBScript operators."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "VBScript Operators"
type = "guides"
weight = 10
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/vbsoperators"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Overview

VBScript has a full range of operators, including arithmetic operators, comparison operators, concatenation operators, and logical operators.

## Operator Precedence

When several operations occur in an expression, each part is evaluated and resolved in a predetermined order called operator precedence.  You can use parentheses to override the order of precedence and force some parts of an expression to be evaluated before others.  Operations within parentheses are always performed before those outside.  Within parentheses, however, standard operator precedence is maintained.

When expressions contain operators from more than one category, arithmetic operators are evaluated first, comparison operators are evaluated next, and logical operators are evaluated last.  Comparison operators all have equal precedence; that is, they are evaluated in the left-to-right order in which they appear.  Arithmetic and logical operators are evaluated in the following order of precedence.

### Arithmetic

| Description |      | Symbol |
| :---------- | ---- | -----: |
 | Exponentiation |    | `^` |
 | Unary negation |    | `-` |
 | Multiplication |    | `*` |
 | Division |    | `/` |
 | Integer division |    | `\` |
 | Modulus arithmetic |    | `Mod` |
 | Addition |    | `+` |
 | Subtraction |    | `-` |
 | String concatenation |    | `&` |


### Comparison

| Description |      | Symbol |
| :---------- | ---- | -----: |
 | Equality |    | `=` |
 | Inequality |    | `<>` |
 | Less than |    | `<` |
 | Greater than |    | `>` |
 | Less than or equal to |    | `<=` |
 | Greater than or equal to |    | `>=` |
 | Object equivalence |    | `Is` |


### Logical

| Description |      | Symbol |
| :---------- | ---- | -----: |
 | Logical negation |   | `Not` |
 | Logical conjunction |    | `And` |
 | Logical disjunction |    | `Or` |
 | Logical exclusion |    | `Xor` |
 | Logical equivalence |    | `Eqv` |
 | Logical implication |    | `Imp` |


## Considerations

When multiplication and division occur together in an expression, each operation is evaluated as it occurs from left to right.  Likewise, when addition and subtraction occur together in an expression, each operation is evaluated in order of appearance from left to right.

The string concatenation (`&`) operator is not an arithmetic operator, but in precedence it falls after all arithmetic operators and before all comparison operators.  The `Is` operator is an object reference comparison operator.  It does not compare objects or their values; it checks only to determine if two object references refer to the same object.

## Related Topics

- [What are VBScript and RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript)
