In Tokyo this month, NVIDIA did something it usually avoids in healthcare: it stopped saying "pilot." Across a dense week of announcements tied to CEO Jensen Huang's visit, the company and its Japanese partners described autonomous surgical robots, AI-accelerated CT scanners, and agentic drug-discovery platforms not as experiments but as products that are shipping. Canon, Fujifilm, Kawasaki Heavy Industries and a roster of top Japanese pharma companies are now selling or deploying NVIDIA-powered medical systems. As NVIDIA put it, AI in Japanese healthcare "is no longer an experiment. It's infrastructure."

Underneath the deployments sits a new full-stack platform for healthcare robotics — a set of datasets, simulators and models purpose-built to teach machines how to operate inside hospitals and operating rooms.

## The stack: Open-H, Cosmos-H, GR00T-H and Project Rheo

The platform mirrors the architecture NVIDIA uses for industrial robots, adapted for clinical work. **Open-H** is described as the largest healthcare robotics dataset assembled to date, with more than 776 hours of annotated surgical video. **Cosmos-H** generates physically accurate synthetic surgical data, letting robots train on procedures and edge cases they have never actually observed. **GR00T-H** is a vision-language-action (VLA) model — a system that ingests a text instruction and a visual scene and outputs precise physical motion — tuned for clinical tasks.

Tying it together is **Project Rheo**, a hospital digital-twin blueprint built on NVIDIA's Isaac Sim and Isaac for Healthcare. Rheo lets developers construct a "SimReady" virtual hospital where robots rehearse thousands of navigation patterns, workflow variations and human interactions before touching a patient. In one reference workflow, a robot picks up a surgical tray in a pre-operative room and places it on a cart; in another, it performs multi-stage bimanual manipulation to assemble a trocar. The pitch is that the messiest, highest-stakes part of medical robotics — real-world validation — can move into simulation first.

NVIDIA reinforced the stack at the SRS 2026 surgical robotics conference with an open-source Medical Physics Simulation framework inside Isaac for Healthcare, which models anatomy, device contact, friction and sensor inputs across hundreds of parallel environments. Early adopters include CMR Surgical, Johnson & Johnson MedTech, Karl Storz's Asensus, Moon Surgical and Xcath.

"Open source models allow us to build on shared knowledge, accelerating responsible innovation and, ultimately, gives us the potential to deliver more consistent care and better outcomes for patients worldwide," said Chris Fryer, chief technology officer of CMR Surgical.

## Japan's medtech giants go into production

The Japanese partners are what make this more than a research release. Kawasaki Heavy Industries is building surgical support, nursing-assistant and hospital-transport robots — its FORRO, Nyokkey and NURABOT lines — on NVIDIA Holoscan IGX, Isaac for Healthcare, Isaac GR00T and Cosmos. Direava, a Japanese startup, is developing a surgical vision-language model for real-time understanding of and natural-language interaction with surgical video.

On imaging, two national champions are shipping, not previewing. Canon launched Japan's first NVIDIA-accelerated photon-counting CT system. Fujifilm commercialized Japan's first whole-body CT system powered by NVIDIA Blackwell, using diffusion-based deep-learning reconstruction to sharpen image quality. Both put AI-accelerated computing directly inside FDA-class hardware sold to hospitals.

## Drug discovery on Tokyo-1

The pharmaceutical side runs on Tokyo-1, the AI drug-discovery consortium operated by Xeureka, which added Eisai in April alongside founding members Astellas, Daiichi Sankyo and Ono Pharmaceutical. All are advancing programs on NVIDIA BioNeMo. Astellas has deployed nearly all of BioNeMo's NIM microservices and is running the BioNeMo Agent Toolkit, which NVIDIA describes as a way to turn any AI agent into "an autonomous life sciences scientist." Ono is using the Boltz-2 microservice; Daiichi Sankyo is running ultralarge-scale virtual screening accelerated by NVIDIA RAPIDS. Biomy, working with the Japanese Foundation for Cancer Research, reported a 90% speedup in spatial transcriptomics analysis and is building a virtual cell foundation model.

## Why embodied AI and healthcare, why Japan

The strategic logic is demographic. Japan is the world's oldest major economy, with a shrinking workforce and mounting care burden. Huang framed the fusion of manufacturing and AI as a direct answer to that squeeze. "Japan has historically been very good at precision manufacturing and very large-scale manufacturing, but now we have AI," he told reporters in Tokyo. "You can combine the two technologies and create robotics. The future of intelligent manufacturing, the future of robotics can now start." Robots, he added, can "augment the workers you have and increase national productivity."

Vision-language-action models are the enabling shift. Earlier surgical AI mostly perceived — flagging tissue, measuring, annotating. A VLA model closes the loop from perception to action, which is precisely what a robot handing over instruments or navigating a ward needs. Doing that safely requires synthetic data and digital twins, because you cannot iterate reinforcement-learning policies on live patients. That is why the Open-H/Cosmos-H/GR00T-H/Rheo bundle matters more than any single robot: it is the training and validation pipeline that makes clinical embodied AI defensible.

## What to watch

Three things. First, regulation: shipping CT scanners is one matter; autonomous, VLA-driven manipulation near patients will test how the FDA and Japan's PMDA treat models trained largely in simulation. Second, whether Japanese pharma's BioNeMo work on Tokyo-1 yields disclosed clinical candidates, not just faster screening. Third, adoption breadth — Kawasaki's transport and nursing robots are the likeliest to scale first, so watch for named hospital deployments and unit numbers over the coming quarters. If those land, "infrastructure" will have earned the word.
