---
title: Introduce 'Ghidra Software Reverse-Egnineering for Beginners' book as a technical reviewer
date: 2026-01-11 15:34:57 +0900
categories: [reviews]
tags: [ghidra, reverse-engineering, technical-review, packt, book-review, cybersecurity]     # TAG names should always be lowercase
published: true
---

# Overview
I had the privilege of serving as a technical reviewer for the newly released book “Ghidra Software Reverse Engineering for Beginners”, published by Packt!

As someone who's spent over a decade in the field of cybersecurity, contributing to this book was both a rewarding and humbling experience. I deeply value opportunities like this to give back to the community and help empower the next generation of reverse engineers.

Whether you're starting your reverse engineering journey or looking to deepen your knowledge using Ghidra, this book is a fantastic resource.

You can find it here:
<https://www.packtpub.com/en-us/product/ghidra-software-reverse-engineering-for-beginners-9781835889824>

![about the reviewer](/assets/img/posts/2026-01-11/20260111-01.png){: width="240" height="120" }

# Who this book is for
This book is intended for security researchers, malware analysts, bug hunters, software engineers,
and cybersecurity professionals or students who are involved in software development, testing, and
security analysis. It is also suitable for individuals aspiring to enter the security industry as malware or
vulnerability researchers. In fact, any person who wants to learn Ghidra by minimizing the learning
curve and starting to write their own tools will certainly enjoy this book and accomplish their goal.
Readers should have prior knowledge of programming in Java or Python and experience with software
development or application programming to fully benefit from the concepts and practical examples
presented here.

# What this book covers
Chapter 1, Getting Started with Ghidra, introduces you to the Ghidra platform and its history, covering
installation procedures and a basic overview of the program from the user perspective.

Chapter 2, Automating RE Tasks with Ghidra Scripts, explores how to use Ghidra’s scripting capabilities
to automate reverse-engineering tasks, and introduces script development.

Chapter 3, Ghidra Debug Mode, delves into how to set up a Ghidra development environment, the
methods for debugging Ghidra, and details regarding the Ghidra debug mode vulnerability.

Chapter 4, Using Ghidra Extensions, provides you with background for developing Ghidra extensions,
as well as showing you how to install and use them.

Chapter 5, Reversing Malware Using Ghidra, demonstrates how to use Ghidra for malware analysis by
reversing a real-world malware sample.

Chapter 6, Scripting Malware Analysis, teaches you how to automate malware analysis with Java
and Python scripts. It builds on the previous chapter by providing scripts for analyzing shellcode in 
malware samples.

Chapter 7, Using Ghidra’s Headless Analyzer, explains how to run Ghidra in headless mode for automated
batch processing and analyzing malware samples using a script developed during the chapter.

Chapter 8, Binary Diffing, explains the Ghidra BSim feature, detailing how to set it up and use it
for analysis. It covers techniques for comparing binaries to identify changes, analyze patches, and
discover vulnerabilities.

Chapter 9, Auditing Program Binaries, introduces the topic of finding memory corruption vulnerabilities
using Ghidra and how to exploit them.

Chapter 10, Scripting Binary Audits, continues the previous chapter, teaching how to automate the
bug-hunting process via scripting, taking advantage of the powerful PCode intermediate representation.

Chapter 11, Developing Ghidra Plugins, provides insights into creating custom plugins to extend
Ghidra’s functionality and tailor it to specific reverse-engineering needs.

Chapter 12, Incorporating New Binary Formats, shows you how to add support for new and custom
binary formats within Ghidra using a real-world example, broadening the scope of your analyses.

Chapter 13, Analyzing Processor Modules, discusses how to write Ghidra processor modules using the
SLEIGH processor specification language.

Chapter 14, Contributing to the Ghidra Community, explains how to interact with the community using
social networks, chats, and how to contribute with your own development, feedback, bug reports,
comments, and so on.

Chapter 15, Extending Ghidra for Advanced Reverse-Engineering, introduces advanced reverse-
engineering topics and tools such as SMT solvers, Microsoft Z3, static and dynamic symbex,
LLVM, and Angr, and explains how to incorporate them with Ghidra.

Chapter 16, Debugging, covers the Ghidra debugging tool and outlines various debugging strategies.
It also describes different debugging modes, including remote and kernel debugging, for analyzing
complex code execution scenarios.

Chapter 17, Unpacking in-the-Wild Malware, teaches you how to unpack and analyze real-world
malware samples, revealing the techniques used by threat actors.

Chapter 18, Reverse-Engineering Ransomware, delves into a detailed analysis of ransomware to
comprehend its internal mechanisms. The chapter also offers an overview of the encryption techniques
utilized by ransomware and methods for identifying encryption algorithms using Ghidra.