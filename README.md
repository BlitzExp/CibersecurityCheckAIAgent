# CibersecurityCheckAIAgent

## Overview
This project implements a local AI-assisted agent that analyzes a project's technology stack
and evaluates the security risk of its dependencies using public vulnerability data.

## Problem
Developers and students often lack a fast, contextual way to understand whether the libraries
they use are affected by known exploits and what actions should be taken.

## Input
A structured JSON file describing the project stack (libraries and versions).

## Output
A security risk report classifying each dependency as:
- SAFE
- DOUBTFUL
- INSECURE

Along with actionable recommendations.

## Architecture
- Deterministic risk evaluation engine
- Passive vulnerability data sources
- Local open-source LLM for explanations

## Ethical Considerations
This agent performs **passive analysis only** using public vulnerability metadata.
No exploit code is executed or downloaded.

## Limitations
This tool does not replace professional security audits or active scanning.
