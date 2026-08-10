---
broader: "[[machine learning]]"
inferred:skos:ancestor: "[[machine learning]]"
inferred:skos:narrower:
  - "[[Excessive latency]]"
  - "[[ML System failures]]"
  - "[[ML system design process]]"
  - "[[Nano-precision detection system]]"
  - "[[Reproducibility]]"
  - "[[best-classification-rate AI detection system]]"
  - "[[cold start problem]]"
  - "[[machine learning systems]]"
---

Important design decisions : 

* cloud  VS. edge based 
* offline VS. online learning 
* batch VS.online predictions 

Modern machine learning systems span a spectrum of deployment options, each with its own set of characteristics and use cases. At one end, we have cloud-based ML, which leverages powerful centralized computing resources for complex, data-intensive tasks. Moving along the spectrum, we encounter edge ML, which brings computation closer to the data source for reduced latency and improved privacy. Mobile ML further extends these capabilities to smartphones and tablets, while at the far end, we find Tiny ML, which enables machine learning on extremely low-power devices with severe memory and processing constraints.

This spectrum of deployment can be visualized like Earth’s geological features, each operating at different scales in our computational landscape. Cloud ML systems operate like continents, processing vast amounts of data across interconnected centers; Edge ML exists where these continental powers meet the sea, creating dynamic coastlines where computation flows into local waters; Mobile ML moves through these waters like ocean currents, carrying computing power across the digital seas; and where these currents meet the physical world, TinyML systems rise like islands, each a precise point of intelligence in the vast computational ocean.

[Figure 2.1](https://mlsysbook.ai/contents/core/ml_systems/ml_systems.html#fig-cloud-edge-TinyML-comparison) illustrates the spectrum of distributed intelligence across these approaches, providing a visual comparison of their characteristics. We will examine the unique characteristics, advantages, and challenges of each approach, as depicted in the figure. Additionally, we will discuss the emerging trends and technologies that are shaping the future of machine learning deployment, considering how they might influence the balance between these three paradigms.

[![](https://mlsysbook.ai/contents/core/ml_systems/images/png/cloud-edge-tiny.png)](https://mlsysbook.ai/contents/core/ml_systems/images/png/cloud-edge-tiny.png "Figure 2.1: Cloud vs. Edge vs. Mobile vs. Tiny ML: The Spectrum of Distributed Intelligence. Source: ABI Research – Tiny ML.")

Figure 2.1: Cloud vs. Edge vs. Mobile vs. Tiny ML: The Spectrum of Distributed Intelligence. Source: ABI Research – Tiny ML.

[](https://mlsysbook.ai/contents/core/ml_systems/ml_systems.html#fig-cloud-edge-TinyML-comparison)

To better understand the dramatic differences between these ML deployment options, [Table 2.1](https://mlsysbook.ai/contents/core/ml_systems/ml_systems.html#tbl-representative-systems) provides examples of representative hardware platforms for each category. These examples illustrate the vast range of computational resources, power requirements, and cost considerations across the ML systems spectrum. As we explore each paradigm in detail, you can refer back to these concrete examples to better understand the practical implications of each approach.

Table 2.1: Representative hardware platforms across the ML systems spectrum, showing typical specifications and capabilities for each category.

|Category|Example Device|Processor|Memory|Storage|Power|Price Range|Example Models/Tasks|
|---|---|---|---|---|---|---|---|
|Cloud ML|NVIDIA DGX A100|8x NVIDIA A100 GPUs (40 GB/80 GB)|1 TB System RAM|15 TB NVMe SSD|6.5 kW|$200 K+|Large language models (GPT-3), real-time video processing|
||Google TPU v4 Pod|4096 TPU v4 chips|128 TB+|Networked storage|~MW|Pay-per-use|Training foundation models, large-scale ML research|
|Edge ML|NVIDIA Jetson AGX Orin|12-core Arm® Cortex®-A78AE, NVIDIA Ampere GPU|32 GB LPDDR5|64GB eMMC|15-60 W|$899|Computer vision, robotics, autonomous systems|
||Intel NUC 12 Pro|Intel Core i7-1260P, Intel Iris Xe|32 GB DDR4|1 TB SSD|28 W|$750|Edge AI servers, industrial automation|
|Mobile ML|iPhone 15 Pro|A17 Pro (6-core CPU, 6-core GPU)|8 GB RAM|128 GB-1 TB|3-5 W|$999+|Face ID, computational photography, voice recognition|
|Tiny ML|Arduino Nano 33 BLE Sense|Arm Cortex-M4 @ 64 MHz|256 KB RAM|1 MB Flash|0.02-0.04 W|$35|Gesture recognition, voice detection|
||ESP32-CAM|Dual-core @ 240MHz|520 KB RAM|4 MB Flash|0.05-0.25 W|$10|Image classification, motion detection|

[](https://mlsysbook.ai/contents/core/ml_systems/ml_systems.html#tbl-representative-systems)

The evolution of machine learning systems can be seen as a progression from centralized to increasingly distributed and specialized computing paradigms:

**Cloud ML**: Initially, ML was predominantly cloud-based. Powerful, scalable servers in data centers are used to train and run large ML models. This approach leverages vast computational resources and storage capacities, enabling the development of complex models trained on massive datasets. Cloud ML excels at tasks requiring extensive processing power, distributed training of large models, and is ideal for applications where real-time responsiveness isn’t critical. Popular platforms like AWS SageMaker, Google Cloud AI, and Azure ML offer flexible, scalable solutions for model development, training, and deployment. Cloud ML can handle models with billions of parameters, training on petabytes of data, but may incur latencies of 100-500 ms for online inference due to network delays.

**Edge ML**: As the need for real-time, low-latency processing grew, Edge ML emerged. This paradigm brings inference capabilities closer to the data source, typically on edge devices such as industrial gateways, smart cameras, autonomous vehicles, or IoT hubs. Edge ML reduces latency (often to less than 50 ms), enhances privacy by keeping data local, and can operate with intermittent cloud connectivity. It’s particularly useful for applications requiring quick responses or handling sensitive data in industrial or enterprise settings. Frameworks like NVIDIA Jetson or Google’s Edge TPU enable powerful ML capabilities on edge devices. Edge ML plays a crucial role in IoT ecosystems, enabling real-time decision making and reducing bandwidth usage by processing data locally.

**Mobile ML**: Building on edge computing concepts, Mobile ML focuses on leveraging the computational capabilities of smartphones and tablets. This approach enables personalized, responsive applications while reducing reliance on constant network connectivity. Mobile ML offers a balance between the power of edge computing and the ubiquity of personal devices. It utilizes on-device sensors (e.g., cameras, GPS, accelerometers) for unique ML applications. Frameworks like TensorFlow Lite and Core ML allow developers to deploy optimized models on mobile devices, with inference times often under 30 ms for common tasks. Mobile ML enhances privacy by keeping personal data on the device and can operate offline, but must balance model performance with device resource constraints (typically 4-8 GB RAM, 100-200 GB storage).

**Tiny ML**: The latest development in this progression is Tiny ML, which enables ML models to run on extremely resource-constrained microcontrollers and small embedded systems. Tiny ML allows for on-device inference without relying on connectivity to the cloud, edge, or even the processing power of mobile devices. This approach is crucial for applications where size, power consumption, and cost are critical factors. Tiny ML devices typically operate with less than 1 MB of RAM and flash memory, consuming only milliwatts of power, enabling battery life of months or years. Applications include wake word detection, gesture recognition, and predictive maintenance in industrial settings. Platforms like Arduino Nano 33 BLE Sense and STM32 microcontrollers, coupled with frameworks like TensorFlow Lite for Microcontrollers, enable ML on these tiny devices. However, Tiny ML requires significant model optimization and quantization[1](https://mlsysbook.ai/contents/core/ml_systems/ml_systems.html#fn1) to fit within these constraints.

1 **Quantization**: Process of reducing the numerical precision of ML model parameters to reduce memory footprint and computational demand.

Each of these paradigms has its own strengths and is suited to different use cases:

- Cloud ML remains essential for tasks requiring massive computational power or large-scale data analysis.
- Edge ML is ideal for applications needing low-latency responses or local data processing in industrial or enterprise environments.
- Mobile ML is suited for personalized, responsive applications on smartphones and tablets.
- Tiny ML enables AI capabilities in small, power-efficient devices, expanding the reach of ML to new domains.

This progression reflects a broader trend in computing towards more distributed, localized, and specialized processing. The evolution is driven by the need for faster response times, improved privacy, reduced bandwidth usage, and the ability to operate in environments with limited or no connectivity, while also catering to the specific capabilities and constraints of different types of devices.

[Figure 2.2](https://mlsysbook.ai/contents/core/ml_systems/ml_systems.html#fig-vMLsizes) illustrates the key differences between Cloud ML, Edge ML, Mobile ML, and Tiny ML in terms of hardware, latency, connectivity, power requirements, and model complexity. As we move from Cloud to Edge to Tiny ML, we see a dramatic reduction in available resources, which presents significant challenges for deploying sophisticated machine learning models. This resource disparity becomes particularly apparent when attempting to deploy deep learning models on microcontrollers, the primary hardware platform for Tiny ML. These tiny devices have severely constrained memory and storage capacities, which are often insufficient for conventional deep learning models. We will learn to put these things into perspective in this chapter.

[![](https://mlsysbook.ai/contents/core/ml_systems/images/jpg/cloud_mobile_tiny_sizes.jpg)](https://mlsysbook.ai/contents/core/ml_systems/images/jpg/cloud_mobile_tiny_sizes.jpg "Figure 2.2: From cloud GPUs to microcontrollers: Navigating the memory and storage landscape across computing devices. Source: [@lin2023tiny]")

Figure 2.2: From cloud GPUs to microcontrollers: Navigating the memory and storage landscape across computing devices. Source: ([Lin et al. 2023](https://mlsysbook.ai/contents/core/references.html#ref-lin2023tiny))