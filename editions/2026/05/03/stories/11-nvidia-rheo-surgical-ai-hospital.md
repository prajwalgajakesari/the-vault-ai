---
headline: "NVIDIA and Advent Health Deploy Multi-Agent Surgical AI Using Rheo Blueprint for Hospital Automation"
slug: nvidia-rheo-surgical-ai-hospital
category: research
story_number: "11"
date: 2026-05-03
sources:
  - name: "NVIDIA National Robotics Week Blog"
    url: "https://blogs.nvidia.com/blog/national-robotics-week-2026/"
    domain: "blogs.nvidia.com"
  - name: "NVIDIA AI in Healthcare Survey 2026"
    url: "https://blogs.nvidia.com/blog/ai-in-healthcare-survey-2026/"
    domain: "blogs.nvidia.com"
  - name: "Proximie x NVIDIA Smart OR Announcement"
    url: "https://www.businesswire.com/news/home/20260420010687/en/Global-Healthtech-Proximie-Advances-the-Intelligent-Operating-Room-of-the-Future-With-NVIDIA"
    domain: "businesswire.com"
  - name: "NVIDIA Isaac for Healthcare Developer Blog"
    url: "https://developer.nvidia.com/blog/using-simulation-to-build-robotic-systems-for-hospital-automation/"
    domain: "developer.nvidia.com"
  - name: "NVIDIA GTC 2026 Isaac GR00T for Surgical Robotics"
    url: "https://www.2minutemedicine.com/nvidia-gtc-2026-unveils-isaac-gr00t-foundation-model-for-surgical-robotics/"
    domain: "2minutemedicine.com"
---

# NVIDIA and Advent Health Deploy Multi-Agent Surgical AI Using Rheo Blueprint for Hospital Automation

*The GPU giant is betting that the future of surgery starts in simulation -- and Project Rheo is its most ambitious healthcare play yet.*

The operating room of the future will not be built by surgeons alone. It will be rehearsed, stress-tested, and continuously optimized by artificial intelligence long before a single patient is wheeled through the door.

That is the premise behind **Project Rheo**, a new NVIDIA blueprint for hospital automation that pairs physical robotic agents with digital AI observers to create what the company calls multi-agent surgical intelligence. Unveiled at NVIDIA GTC 2026 in March and now entering early deployment with partners including **AdventHealth** and **Lightwheel**, the initiative represents a significant escalation in NVIDIA's push to become the infrastructure backbone of AI-driven healthcare.

## From Digital Twin to Surgical Suite

Project Rheo is built on **NVIDIA Isaac for Healthcare**, the company's dedicated robotics development platform that extends Isaac Sim and Isaac Lab into clinical environments. The platform enables multi-scale simulation spanning everything from individual surgical instruments to full hospital floor plans, including operating rooms, intensive care units, sterile processing departments, and labs.

The workflow follows five deliberate steps: create a digital twin of the hospital environment, capture expert demonstrations using controllers, multiply that experience through synthetic data generation, train policies using NVIDIA's **GR00T vision-language-action models**, and validate thoroughly before any real-world deployment.

This simulation-first philosophy is not incidental -- it is the core design constraint. Rather than iterating with robots inside live clinical settings, Rheo lets development teams run thousands of navigation patterns, workflow variations, and human interaction scenarios in silico. The approach directly addresses one of healthcare robotics' most persistent bottlenecks: the near-impossibility of collecting large-scale training data in active hospitals without disrupting patient care.

## Lightwheel and AdventHealth: Intelligence in the OR

The partnership between **Lightwheel**, **AdventHealth**, and NVIDIA brings embodied intelligence directly into the operating room. The collaboration focuses on supporting surgical teams with situational awareness, sterile coordination, and intelligent management of instruments, implants, and workflows -- crucially, automating the support infrastructure around surgery rather than the procedure itself.

Using Isaac for Healthcare and the Rheo blueprint, the team is developing multi-agent systems that can sense, coordinate, and act in real time. Physical agents handle tasks such as surgical tray pick-and-place, case cart transport, and bimanual tool handling, while digital agents observe camera feeds and suggest next actions to clinical staff.

## Proximie's Ambient Surgical Intelligence

Another major Project Rheo partner, **Proximie**, is contributing what may be the initiative's most valuable asset: real-world surgical data at scale. Proximie's Intelligence Suite operates as an ambient AI layer inside live ORs across hundreds of healthcare facilities worldwide, continuously capturing intraoperative video, workflow activity, instrument usage, and procedural context.

NVIDIA supplies the infrastructure that makes this data AI-ready and enables synthetic augmentation via the open **Cosmos** platform. Together, the partners are developing a vision-language model that monitors OR activity in real time and recognizes key surgical milestones.

The early results are compelling. Proximie platform users have reported **OR productivity improvements of up to 24%**, unlocking as many as **300 additional procedures per OR per year** through better visibility into workflows and more accurate predictions of surgery duration.

## The Numbers Behind the Push

NVIDIA's urgency is backed by stark industry data. The company's own **2026 State of AI in Healthcare survey** found that **63% of healthcare professionals are already actively using AI**, with another 31% piloting or evaluating initiatives. A full **85% of respondents said their AI budgets would increase** this year, and nearly half (46%) expect spending to jump by more than 10%.

The workforce math is equally pressing. The World Health Organization projects a shortage of **11 million healthcare workers by 2030**. Hospitals cannot simply hire their way out of the efficiency gap -- they need systems that amplify the capacity of the staff they have.

Meanwhile, the ecosystem around NVIDIA's healthcare robotics platform continues to expand. **CMR Surgical** is using Cosmos-H simulation for its Versius surgical system. **Johnson & Johnson MedTech** is training systems for the Monarch Platform for Urology using Isaac Sim workflows. **Medtronic** is exploring NVIDIA's **IGX Thor** platform to deliver mission-critical precision in surgical robotics.

## What It Means

Project Rheo is not a product launch -- it is a platform play. NVIDIA is positioning itself as the simulation-to-deployment pipeline for an entire class of healthcare robotics that does not fully exist yet. By providing the digital twin infrastructure, the foundation models, and the compute layer, the company is making a bet that whoever controls the training environment will ultimately shape how AI enters the hospital.

The risk is real: healthcare's regulatory landscape, data privacy requirements (cited as a top challenge by 39% of survey respondents), and the sheer complexity of clinical workflows mean that the gap between simulation and certified deployment remains wide. But if the Proximie productivity numbers hold at scale, the economic argument for multi-agent surgical AI may prove irresistible.

For hospital systems watching their staffing ratios deteriorate and their procedure backlogs grow, Project Rheo offers something rare in healthcare AI: a path from proof-of-concept to production that does not require experimenting on patients first.
