# Maruvi - AI Prescription Safety Assistant
## Software Requirements Document

### 1. Problem Statement

Patients often struggle to understand their prescriptions, leading to medication errors, missed doses, and confusion about drug interactions. Traditional prescriptions use medical terminology that is difficult for non-medical professionals to comprehend. There is a critical need for an accessible, intelligent system that can:

- Interpret prescription images and extract medication information
- Translate complex medical terminology into plain language
- Provide safety information and potential warnings
- Help patients manage their medication schedules effectively
- Be accessible through popular messaging platforms

### 2. Project Overview

Maruvi is an AI-powered prescription safety assistant designed to bridge the gap between medical prescriptions and patient understanding. The system leverages cloud-based AI services to provide instant, accurate medication information through conversational interfaces on WhatsApp and Telegram.

### 3. Goals and Objectives

#### Primary Goals
- Enable patients to understand their prescriptions without medical expertise
- Reduce medication errors through clear explanations and safety warnings
- Improve medication adherence through automated reminders
- Provide 24/7 accessible medication information

#### Success Metrics
- Accurate text extraction from prescription images (>95% accuracy)
- Response time under 5 seconds for prescription analysis
- User satisfaction rating above 4.5/5
- System uptime of 99.5% or higher

### 4. Functional Requirements

#### 4.1 Prescription Image Processing
- **FR-1.1**: System shall accept prescription images in JPEG, PNG, and PDF formats
- **FR-1.2**: System shall extract text from prescription images using OCR technology
- **FR-1.3**: System shall identify medication names, dosages, and instructions from extracted text
- **FR-1.4**: System shall handle handwritten and printed prescriptions
- **FR-1.5**: System shall support images up to 10MB in size

#### 4.2 Medicine Information Explanation
- **FR-2.1**: System shall provide plain language explanations for each medication
- **FR-2.2**: System shall explain the purpose and use of each medicine
- **FR-2.3**: System shall present information in user's preferred language
- **FR-2.4**: System shall break down complex medical terms into simple language
- **FR-2.5**: System shall provide audio explanations using text-to-speech

#### 4.3 Active Ingredients Display
- **FR-3.1**: System shall identify and display active ingredients for each medication
- **FR-3.2**: System shall show generic names alongside brand names
- **FR-3.3**: System shall indicate ingredient concentrations and strengths
- **FR-3.4**: System shall highlight common allergens in ingredients

#### 4.4 Safety Information
- **FR-4.1**: System shall provide safety warnings for each medication
- **FR-4.2**: System shall identify potential drug interactions when multiple medications are present
- **FR-4.3**: System shall display common side effects
- **FR-4.4**: System shall provide contraindications and precautions
- **FR-4.5**: System shall include storage instructions
- **FR-4.6**: System shall warn about pregnancy/breastfeeding considerations

#### 4.5 Medication Reminders
- **FR-5.1**: System shall generate medication schedules based on prescription instructions
- **FR-5.2**: System shall send reminder notifications at scheduled times
- **FR-5.3**: System shall allow users to customize reminder times
- **FR-5.4**: System shall track medication adherence
- **FR-5.5**: System shall support multiple concurrent medication schedules
- **FR-5.6**: System shall allow users to mark doses as taken or skipped

#### 4.6 Chatbot Interface
- **FR-6.1**: System shall operate as a WhatsApp chatbot
- **FR-6.2**: System shall operate as a Telegram chatbot
- **FR-6.3**: System shall support conversational queries about medications
- **FR-6.4**: System shall handle image uploads through chat interface
- **FR-6.5**: System shall provide interactive menu options for common actions
- **FR-6.6**: System shall maintain conversation context across messages
- **FR-6.7**: System shall support multi-turn conversations for clarifications

#### 4.7 User Management
- **FR-7.1**: System shall create user profiles upon first interaction
- **FR-7.2**: System shall store user prescription history
- **FR-7.3**: System shall allow users to view past prescriptions
- **FR-7.4**: System shall support multiple prescriptions per user
- **FR-7.5**: System shall allow users to delete their data

### 5. Non-Functional Requirements

#### 5.1 Performance
- **NFR-1.1**: Image processing shall complete within 3 seconds
- **NFR-1.2**: AI response generation shall complete within 2 seconds
- **NFR-1.3**: System shall handle 1000 concurrent users
- **NFR-1.4**: Database queries shall return results within 500ms

#### 5.2 Scalability
- **NFR-2.1**: System shall scale horizontally to handle increased load
- **NFR-2.2**: Architecture shall support serverless auto-scaling
- **NFR-2.3**: System shall handle 10,000 requests per day initially
- **NFR-2.4**: System shall be designed to scale to 100,000+ daily users

#### 5.3 Security and Privacy
- **NFR-3.1**: All data shall be encrypted in transit using TLS 1.3
- **NFR-3.2**: All data shall be encrypted at rest using AES-256
- **NFR-3.3**: System shall comply with HIPAA privacy requirements
- **NFR-3.4**: Prescription images shall be deleted after processing (optional retention with consent)
- **NFR-3.5**: User data shall be isolated and access-controlled
- **NFR-3.6**: System shall implement authentication for API access
- **NFR-3.7**: Audit logs shall be maintained for all data access

#### 5.4 Reliability
- **NFR-4.1**: System shall maintain 99.5% uptime
- **NFR-4.2**: System shall implement automatic failover mechanisms
- **NFR-4.3**: System shall have backup and disaster recovery procedures
- **NFR-4.4**: Failed operations shall be retried automatically

#### 5.5 Usability
- **NFR-5.1**: Chatbot responses shall be clear and conversational
- **NFR-5.2**: System shall provide help commands and guidance
- **NFR-5.3**: Error messages shall be user-friendly and actionable
- **NFR-5.4**: Interface shall be accessible to users with varying technical literacy

#### 5.6 Maintainability
- **NFR-6.1**: Code shall follow AWS best practices
- **NFR-6.2**: System shall use infrastructure as code (IaC)
- **NFR-6.3**: Components shall be loosely coupled and independently deployable
- **NFR-6.4**: System shall include comprehensive logging and monitoring

### 6. User Stories

#### As a Patient
- **US-1**: As a patient, I want to upload a photo of my prescription so that I can understand what medications I need to take
- **US-2**: As a patient, I want to receive explanations in simple language so that I can understand my medications without medical knowledge
- **US-3**: As a patient, I want to know the side effects of my medications so that I can be aware of what to expect
- **US-4**: As a patient, I want to receive reminders to take my medications so that I don't forget doses
- **US-5**: As a patient, I want to ask questions about my medications so that I can clarify any doubts
- **US-6**: As a patient, I want to hear medication information read aloud so that I can understand even if I have difficulty reading

#### As a Caregiver
- **US-7**: As a caregiver, I want to manage medication schedules for my family members so that I can ensure they take medications correctly
- **US-8**: As a caregiver, I want to check for drug interactions so that I can prevent harmful combinations
- **US-9**: As a caregiver, I want to access prescription history so that I can track medication changes over time

#### As a Healthcare Provider
- **US-10**: As a healthcare provider, I want patients to better understand their prescriptions so that medication adherence improves
- **US-11**: As a healthcare provider, I want patients to have access to safety information so that they can use medications responsibly

### 7. System Architecture and Technology Stack

#### 7.1 AWS Services
- **AWS Textract**: Optical Character Recognition for prescription image processing
- **AWS Bedrock**: AI/ML service for natural language processing and explanation generation
- **AWS Polly**: Text-to-speech service for audio explanations
- **AWS Lambda**: Serverless compute for business logic
- **Amazon DynamoDB**: NoSQL database for user data and prescription storage
- **Amazon S3**: Object storage for prescription images (if retained)
- **Amazon EventBridge**: Event-driven architecture for reminders
- **AWS Secrets Manager**: Secure storage for API keys and credentials
- **Amazon CloudWatch**: Monitoring and logging

#### 7.2 External Integrations
- **WhatsApp Business API**: Primary chatbot interface
- **Telegram Bot API**: Secondary chatbot interface
- **Drug Information API**: External medical database for medication information

### 8. System Constraints

#### 8.1 Technical Constraints
- **C-1**: System must operate within AWS infrastructure
- **C-2**: OCR accuracy depends on prescription image quality
- **C-3**: Response quality depends on AI model capabilities
- **C-4**: WhatsApp/Telegram API rate limits apply
- **C-5**: Text-to-speech supports limited languages

#### 8.2 Regulatory Constraints
- **C-6**: System must comply with healthcare data regulations (HIPAA, GDPR)
- **C-7**: System must include medical disclaimer (not a substitute for professional advice)
- **C-8**: System cannot provide diagnostic or prescribing capabilities
- **C-9**: System must maintain audit trails for compliance

#### 8.3 Business Constraints
- **C-10**: Initial launch limited to specific geographic regions
- **C-11**: AWS service costs must remain within budget
- **C-12**: System must be maintainable by small development team

### 9. Assumptions and Dependencies

#### 9.1 Assumptions
- Users have access to WhatsApp or Telegram
- Users can capture clear images of prescriptions
- Prescriptions follow standard medical formatting
- Users have basic smartphone literacy
- Internet connectivity is available for users

#### 9.2 Dependencies
- AWS service availability and reliability
- WhatsApp/Telegram API stability
- Third-party drug information database accuracy
- AI model performance and updates
- Regulatory approval for healthcare applications

### 10. Future Scope and Enhancements

#### 10.1 Phase 2 Features
- **FS-1**: Integration with pharmacy systems for prescription fulfillment
- **FS-2**: Telemedicine integration for doctor consultations
- **FS-3**: Health tracking and medication effectiveness monitoring
- **FS-4**: Family account management with multiple profiles
- **FS-5**: Integration with wearable devices for health data

#### 10.2 Phase 3 Features
- **FS-6**: AI-powered drug interaction prediction using patient history
- **FS-7**: Personalized medication recommendations based on health data
- **FS-8**: Multi-language support for 20+ languages
- **FS-9**: Voice-based prescription upload and queries
- **FS-10**: Integration with electronic health records (EHR)

#### 10.3 Platform Expansion
- **FS-11**: Native mobile applications (iOS/Android)
- **FS-12**: Web portal for detailed medication management
- **FS-13**: SMS-based interface for users without smartphones
- **FS-14**: Integration with other messaging platforms (Facebook Messenger, WeChat)

#### 10.4 Advanced Features
- **FS-15**: Machine learning for personalized safety warnings based on user profile
- **FS-16**: Blockchain integration for prescription verification
- **FS-17**: Community features for medication reviews and experiences
- **FS-18**: Insurance integration for cost estimation
- **FS-19**: Medication cost comparison across pharmacies
- **FS-20**: Refill reminders and automatic reordering

### 11. Acceptance Criteria

#### 11.1 Minimum Viable Product (MVP)
The system shall be considered ready for initial release when:
- Prescription images can be processed with >90% accuracy
- Medicine explanations are generated in plain language
- Active ingredients are correctly identified
- Basic safety warnings are provided
- Medication reminders can be set and delivered
- WhatsApp chatbot is fully functional
- User data is securely stored and encrypted
- System meets performance requirements (response time <5s)

#### 11.2 Quality Gates
- All functional requirements (FR-1 through FR-7) are implemented
- Security requirements (NFR-3) are fully satisfied
- System passes penetration testing
- User acceptance testing achieves >80% satisfaction
- System handles error cases gracefully
- Documentation is complete for users and developers

### 12. Glossary

- **OCR**: Optical Character Recognition - technology to extract text from images
- **Active Ingredient**: The chemical component in a medication that produces therapeutic effects
- **Drug Interaction**: When one medication affects how another medication works
- **Contraindication**: A condition or factor that makes a particular treatment inadvisable
- **Adherence**: The degree to which a patient follows medication instructions
- **HIPAA**: Health Insurance Portability and Accountability Act - US healthcare privacy law
- **GDPR**: General Data Protection Regulation - EU data privacy regulation
- **Serverless**: Cloud computing model where infrastructure is managed by the provider
- **TTS**: Text-to-Speech - technology that converts text into spoken audio

### 13. Risks and Mitigation

#### 13.1 Technical Risks
- **Risk**: OCR accuracy issues with handwritten prescriptions
  - **Mitigation**: Implement confidence scoring and request clarification for low-confidence results
- **Risk**: AI model hallucinations or incorrect information
  - **Mitigation**: Validate AI responses against trusted drug databases; include disclaimers
- **Risk**: Service outages affecting availability
  - **Mitigation**: Implement multi-region deployment and failover mechanisms

#### 13.2 Compliance Risks
- **Risk**: Healthcare data privacy violations
  - **Mitigation**: Implement comprehensive security controls; regular compliance audits
- **Risk**: Providing medical advice without proper disclaimers
  - **Mitigation**: Clear disclaimers in all communications; limit scope to information only

#### 13.3 User Experience Risks
- **Risk**: Users misunderstanding medication information
  - **Mitigation**: Use clear language; provide examples; allow follow-up questions
- **Risk**: Over-reliance on system instead of consulting healthcare providers
  - **Mitigation**: Regular reminders to consult healthcare professionals; clear scope limitations

---

**Document Version**: 1.0  
**Last Updated**: February 15, 2026  
**Status**: Draft  
**Owner**: Maruvi Development Team
