---
foundationalPaper: The DevOps Handbook (Kim, Humble, Debois & Willis, 2016)
keyPapers:
  - "Continuous Delivery: Reliable Software Releases (Humble & Farley, 2010)"
  - Site Reliability Engineering (Beyer et al., 2016)
  - The Phoenix Project (Kim et al., 2013)
combines:
  - "[[Development]]"
  - "[[Operations]]"
enables:
  - "[[Continuous Integration]]"
  - "[[Continuous Deployment]]"
  - "[[Infrastructure as Code]]"
practices:
  - "[[automation]]"
  - "[[Monitoring]]"
  - "[[version control]]"
  - "[[Collaboration]]"
tools:
  - "[[Docker]]"
  - "[[Kubernetes]]"
  - "[[Jenkins]]"
  - "[[Git]]"
  - "[[Ansible]]"
evolution: "[[MLOps]]"
broader: "[[application development]]"
inferred:skos:ancestor:
  - "[[Process]]"
  - "[[application development]]"
---

# DevOps

DevOps is a set of practices that combines software development (Dev) and IT operations (Ops) to shorten the development lifecycle and provide continuous delivery with high software quality.

## Original Definition

From the DevOps Handbook (2016):
"DevOps is the outcome of applying the most trusted principles from the domain of physical manufacturing and leadership to the IT value stream. DevOps relies on bodies of knowledge from Lean, Theory of Constraints, the Toyota Production System, resilience engineering, learning organizations, safety culture, human factors, and many others."

From Humble & Farley (2010):
"The goal of DevOps is to create a working environment where building, testing, and releasing software can happen rapidly, frequently, and more reliably."

## Historical Development

1. **Agile Movement (2001)**: Foundation principles
2. **Continuous Integration (2006)**: Automated builds
3. **DevOps Term Coined (2009)**: Patrick Debois
4. **Infrastructure as Code (2011)**: Configuration management
5. **Site Reliability Engineering (2016)**: Google's approach

## Core Principles

From the DevOps Handbook:

### The Three Ways
1. **Flow**: Fast flow from development to operations
2. **Feedback**: Fast and constant feedback
3. **Continual Learning**: Culture of experimentation

### CALMS Framework
- **Culture**: Collaboration and shared responsibility
- **Automation**: Repetitive tasks automated
- **Lean**: Waste elimination
- **Measurement**: Data-driven decisions
- **Sharing**: Knowledge and tools

## Key Practices

### Continuous Integration/Continuous Deployment (CI/CD)
From Humble & Farley:
"Every commit should trigger a build of the software and a series of automated tests. If the build or tests fail, the team stops and fixes the problem immediately."

### Infrastructure as Code (IaC)
"Managing and provisioning infrastructure through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools."

### Monitoring and Logging
From SRE book:
"Monitoring is one of the primary means by which service owners keep track of a system's health and availability."

## Technical Components

1. **Version Control**: Git, SVN
2. **CI/CD Pipelines**: Jenkins, GitLab CI
3. **Configuration Management**: Ansible, Chef, Puppet
4. **Containerization**: Docker, containerd
5. **Orchestration**: Kubernetes, Docker Swarm
6. **Monitoring**: Prometheus, Grafana, ELK Stack

## Cultural Aspects

From The Phoenix Project:
1. **Shared Responsibility**: "You build it, you run it"
2. **Blameless Postmortems**: Learn from failures
3. **Continuous Improvement**: Kaizen mindset
4. **Cross-functional Teams**: Breaking down silos

## Metrics and Measurement

### Four Key Metrics (DORA)
1. **Deployment Frequency**: How often code is deployed
2. **Lead Time**: Time from commit to production
3. **Mean Time to Recovery**: Time to restore service
4. **Change Failure Rate**: Percentage of failed changes

## Benefits

From empirical studies:
1. **Faster Time to Market**: Reduced deployment cycles
2. **Improved Quality**: Automated testing
3. **Higher Reliability**: Better monitoring
4. **Enhanced Collaboration**: Shared goals
5. **Reduced Costs**: Automation efficiency

## Challenges

1. **Cultural Resistance**: Organizational change
2. **Tool Complexity**: Integration challenges
3. **Skill Gaps**: Cross-functional expertise
4. **Legacy Systems**: Technical debt
5. **Security Concerns**: "DevSecOps" emergence

## Evolution to MLOps

DevOps principles applied to machine learning:
1. **Data Versioning**: DVC, MLflow
2. **Model Registry**: Model lifecycle management
3. **Feature Stores**: Feature management
4. **Pipeline Orchestration**: Kubeflow, Airflow
5. **Model Monitoring**: Drift detection

## Historical Significance

DevOps transformed:
- Software delivery speed
- Operation reliability
- Team collaboration
- Business agility
- Technical culture

As Gene Kim noted: "DevOps is not a goal, but a never-ending process of continual improvement."

## Modern Practices

1. **GitOps**: Git as single source of truth
2. **Platform Engineering**: Self-service platforms
3. **DevSecOps**: Integrated security
4. **AIOps**: AI-powered operations
5. **Cloud-Native DevOps**: Microservices architecture

The DevOps movement continues to evolve, incorporating new technologies and practices while maintaining its core principles of collaboration, automation, and continuous improvement.
