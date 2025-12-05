

LANG_PATTERNS = {
    # 1. Python
    "python": [
        ("def ", 2),
        ("import ", 1),
        ("class ", 1),
        (":\n", 1),
        ("self", 1),
        ("print(", 1),
    ],

    # 2. JavaScript
    "javascript": [
        ("function", 2),
        ("console.log", 2),
        ("=>", 2),
        ("export ", 1),
        ("import ", 1),
        ("let ", 1),
        ("const ", 1),
    ],

    # 3. TypeScript
    "typescript": [
        (": number", 2),
        (": string", 2),
        ("interface ", 2),
        ("export ", 1),
        ("import ", 1),
        ("implements ", 1),
    ],

    # 4. C
    "c": [
        ("#include", 2),
        ("int main", 2),
        (";", 1),
        ("{}", 1),
        ("printf(", 1),
    ],

    # 5. C++
    "cpp": [
        ("#include <iostream>", 3),
        ("std::", 2),
        ("using namespace", 2),
        ("template <", 2),
        ("cout <<", 1),
    ],

    # 6. Java
    "java": [
        ("public static void main", 3),
        ("class ", 1),
        ("System.out.println", 2),
        ("import java.", 1),
        ("extends ", 1),
        ("implements ", 1),
    ],

    # 7. C#
    "csharp": [
        ("using System;", 3),
        ("namespace ", 2),
        ("public class ", 2),
        ("Console.WriteLine", 2),
        ("; ", 1),
    ],

    # 8. Go
    "go": [
        ("package main", 3),
        ("func main", 2),
        (":=", 2),
        ("fmt.", 1),
        ("import (", 1),
    ],

    # 9. Rust
    "rust": [
        ("fn main", 3),
        ("let mut", 2),
        ("::", 2),
        ("=>", 1),
        ("println!", 1),
    ],

    # 10. PHP
    "php": [
        ("<?php", 3),
        ("echo ", 1),
        ("function ", 1),
        ("$", 1),
        ("->", 1),
    ],

    # 11. Ruby
    "ruby": [
        ("def ", 2),
        ("end", 1),
        ("puts ", 1),
        ("class ", 1),
        (":symbol", 1),
    ],

    # 12. Swift
    "swift": [
        ("import Foundation", 2),
        ("class ", 1),
        ("func ", 2),
        ("let ", 1),
        ("var ", 1),
    ],

    # 13. Kotlin
    "kotlin": [
        ("fun main", 2),
        ("class ", 1),
        ("val ", 2),
        ("var ", 1),
        ("println(", 1),
    ],

    # 14. HTML
    "html": [
        ("<html", 3),
        ("<body", 2),
        ("<div", 1),
        ("</", 1),
        ("<!DOCTYPE html>", 3),
    ],

    # 15. CSS
    "css": [
        ("{", 1),
        ("}", 1),
        (";", 1),
        (": ", 1),
        ("/*", 1),
        ("@media", 2),
    ],

    # 16. JSON
    "json": [
        ("{", 1),
        ("}", 1),
        (":", 1),
        ("\"", 1),
        ("[", 1),
        ("]", 1),
    ],

    # 17. YAML
    "yaml": [
        (": ", 2),
        ("- ", 1),
        ("key:", 1),
        ("true", 1),
        ("false", 1),
    ],

    # 18. XML
    "xml": [
        ("<?xml", 3),
        ("</", 2),
        ("<", 1),
        ("<tag", 1),
    ],

    # 19. Bash / Shell
    "bash": [
        ("#!/bin/bash", 3),
        ("echo ", 1),
        ("$", 1),
        ("fi", 1),
        ("then", 1),
    ],

    # 20. SQL
    "sql": [
        ("SELECT ", 2),
        ("INSERT INTO", 2),
        ("CREATE TABLE", 3),
        ("WHERE ", 1),
        ("FROM ", 1),
    ],
}

def detect_programming_language(file):
    
    with open(file, 'r') as f:
        content = f.read()
        scores = {}
        for lang, patterns in LANG_PATTERNS.items():
            score = 0
            for pattern, weight in patterns:
                occurrences = content.count(pattern)
                score += occurrences * weight
            scores[lang] = score
        detected_language = max(scores, key=scores.get)
    return detected_language
