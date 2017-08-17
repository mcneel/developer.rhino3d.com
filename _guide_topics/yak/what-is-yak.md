---
title: What is Yak?
description: This guide introduces the Yak package manager.
authors: ['Will Pearson']
author_contacts: ['will']
sdk: ['Yak']
languages: # empty
platforms: ['Windows']
categories: ['Overview']
order: 1
keywords: ['developer', 'yak']
layout: toc-guide-page
---

## Overview

Yak is a package manager for the Rhino ecosystem.Yak assists in the discovery, installation, and management of Rhino and Grasshopper packages. Examples of packages are plug-ins, components, scripts, and material definitions. Not wanting to reinvent the
wheel we've taken inspiration from Linux and the software development world in
general. The package manager has several goals.

- Make it easier for users to discover and manage plug-ins and more
- Help developers to share their work
- Provide simple tools that can be used for system administration

The package management system can be broken down into three main areas.

1. [Server](#server)
2. [Command line tool](#command-line-tool)
3. [Integrations](#integrations)

## Server

The package server is the heart of the system. It can be hosted almost anywhere
and keeps the packages organised for its clients – the command line tool and
Rhino (via integrations).

## Command Line Tool

The command line tool provides a basic interface but with full functionality.
It is modelled on well known domain-specific package managers such as Ruby's
`gem` and Python's `pip`. It communicates with the server as well as hooking
into Rhino Accounts for authentication.

## Integrations

Built on top of the same code that is used by the command line tool,
integrations provide direct access to the package ecosystem from inside of
Rhino.

Thus far Yak has been integrated into Grasshopper's "Unrecognized Objects"
dialog, providing [package restore](../package-restore-in-grasshopper)
functionality.
