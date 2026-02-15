# Maruvi - AI Prescription Safety Assistant
## Technical Design Document

### 1. Executive Summary

Maruvi is a serverless, AI-powered prescription safety assistant built on AWS infrastructure. The system processes prescription images, extracts medication information, provides intelligent explanations, and delivers medication reminders through WhatsApp and Telegram chatbot interfaces. This document outlines the technical architecture, design decisions, and implementation strategy optimized for rapid hackathon development.

**Key Technologies**: AWS Lambda, Textract, Bedrock, Polly, DynamoDB, EventBridge, API Gateway

**Target Deployment**: Serverless architecture with auto-scaling capabilities

**Development Timeline**: Hackathon-optimized (48-72 hours)

### 2. Architecture Overview

#### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        User Interface Layer                      │
│                  (WhatsApp / Telegram Chatbots)                 │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                     API Gateway Layer                            │
│              (Webhook Endpoints + Authentication)                │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Lambda Function Layer                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Webhook    │  │  Prescription│  │   Reminder   │         │
│  │   Handler    │  │  Processor   │  │   Scheduler  │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    AWS AI Services Layer                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Textract   │  │   Bedrock    │  │    Polly     │         │
│  │     (OCR)    │  │  (AI/NLP)    │  │    (TTS)     │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└─────────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Data Storage Layer                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  DynamoDB    │  │      S3      │  │ EventBridge  │         │
│  │  (User Data) │  │   (Images)   │  │  (Reminders) │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└─────────────────────────────────────────────────────────────────┘
```

#### 2.2 Component Responsibilities

