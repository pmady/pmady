<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Pavan%20Madduri&fontSize=60&fontColor=fff&animation=twinkling&fontAlignY=35&desc=GPU%2FAI%20Infrastructure%20%7C%20CNCF%20Golden%20Kubestronaut%20%7C%20Open-Source%20Builder&descAlignY=55&descSize=18" width="100%" />
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=00B4D8&center=true&vCenter=true&width=750&height=45&lines=Senior+Cloud+Platform+Engineer+%40+Grainger;CNCF+Golden+Kubestronaut+%C2%B7+Oracle+ACE+Associate;31%2B+PRs+across+17+CNCF+%26+ASWF+projects;GPU+scheduling+%C2%B7+KEDA+%C2%B7+Volcano+%C2%B7+HAMi;Building+GPU+autoscalers+for+Kubernetes+at+scale" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/pavanmadduri/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://pavanmadduri.wordpress.com/">
    <img src="https://img.shields.io/badge/Blog-21759B?style=for-the-badge&logo=wordpress&logoColor=white" />
  </a>
  <a href="https://medium.com/@pavan4devops">
    <img src="https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white" />
  </a>
  <a href="https://dev.to/pavan_madduri">
    <img src="https://img.shields.io/badge/Dev.to-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white" />
  </a>
  <a href="https://hub.docker.com/u/pmady7389">
    <img src="https://img.shields.io/badge/Docker_Hub-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  </a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=pmady&label=Profile+Views&color=00B4D8&style=flat" alt="profile views" />
  &nbsp;
  <a href="https://github.com/pmady?tab=followers">
    <img src="https://img.shields.io/github/followers/pmady?label=Followers&style=social" />
  </a>
</p>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,11,20&height=3&section=header" width="100%" />

---

<p align="center">
  Senior Cloud Platform Engineer building GPU/AI infrastructure at scale.<br/>
  CNCF Golden Kubestronaut. Oracle ACE Associate. Dragonfly Community Member.<br/>
  31+ PRs across 17 open-source projects in CNCF, ASWF, and beyond.<br/>
  If GPUs need scheduling, scaling, or observability on Kubernetes — that's what I build.
</p>

---

## ⚡ What I'm Building

| | |
|--------|------------|
| 🎮 **GPU Autoscaling** | KEDA External Scaler with native NVML metrics, DaemonSet architecture, scaling profiles for vLLM, Triton, and training workloads. Referenced in KEDA #7538 and published on CNCF Blog. |
| 🔬 **GPU NUMA Topology** | Volcano scheduler plugin for NUMA-aware GPU placement — topology discovery via sysfs, CRD extensions, and cross-socket affinity optimization. |
| 📡 **GPU Observability** | OpenTelemetry Collector receiver for GPU metrics (NVML-native) and Docker Desktop Extension for real-time GPU monitoring dashboards. |
| 🧠 **Topology-Aware AIOps** | Knowledge graph of Kubernetes resources with graph-based root-cause traversal, AlertManager webhook integration, and blast-radius analysis. |
| ☁️ **Platform Engineering** | Kubernetes, ArgoCD, Crossplane, Docker, KEDA — production platforms serving enterprise workloads at scale. |
| 📝 **Technical Writing** | Published across CNCF Blog, Platform Engineering, Cloud Native Now, and Medium. |

---

## 🏆 Certifications & Recognition

<p align="left">
  <a href="https://www.cncf.io/training/kubestronaut/?p=pavan-madduri">
    <img src="https://img.shields.io/badge/CNCF-Golden_Kubestronaut-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" />
  </a>
  <a href="https://ace.oracle.com/ords/ace/profile/pavan27">
    <img src="https://img.shields.io/badge/Oracle_ACE-Associate-C74634?style=for-the-badge&logo=oracle&logoColor=white" />
  </a>
  <a href="https://www.cncf.io/people/contributors/">
    <img src="https://img.shields.io/badge/CNCF-Contributor-172B4D?style=for-the-badge&logo=cncf&logoColor=white" />
  </a>
  <a href="https://github.com/dragonflyoss">
    <img src="https://img.shields.io/badge/Dragonfly-Community_Member-1DB954?style=for-the-badge&logoColor=white" />
  </a>
</p>

> **Golden Kubestronaut** — All five Kubernetes certifications: KCNA, CKA, CKAD, CKS, KCSA

---

## 🚀 Featured Projects

<table>
<tr>
<td width="50%">

### 🎮 [KEDA GPU Scaler](https://github.com/pmady/keda-gpu-scaler)

[![Stars](https://img.shields.io/github/stars/pmady/keda-gpu-scaler?style=social)](https://github.com/pmady/keda-gpu-scaler)
[![CI](https://github.com/pmady/keda-gpu-scaler/actions/workflows/ci.yaml/badge.svg)](https://github.com/pmady/keda-gpu-scaler)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**KEDA External gRPC Scaler for GPU/AI workloads**

- 🎮 **Native NVML** — Direct GPU metrics via go-nvml
- 🚀 **Scaling Profiles** — vLLM, Triton, training presets
- 📦 **DaemonSet** — Per-node GPU metric collection
- 🔄 **Scale-to-Zero** — GPU-aware idle detection
- 📈 **Prometheus** — Optional /metrics endpoint

**Tech:** Go · gRPC · NVIDIA NVML · Kubernetes · Helm

**Referenced in** [KEDA #7538](https://github.com/kedacore/keda/issues/7538) | [CNCF Blog](https://www.cncf.io/blog/2026/05/27/gpu-autoscaling-on-kubernetes-with-keda-building-an-external-scaler/)

</td>
<td width="50%">

### 📡 [OpenTelemetry GPU Receiver](https://github.com/pmady/otel-gpu-receiver)

[![Stars](https://img.shields.io/github/stars/pmady/otel-gpu-receiver?style=social)](https://github.com/pmady/otel-gpu-receiver)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**OpenTelemetry Collector receiver for GPU metrics**

- 🔋 **NVIDIA NVML** — GPU utilization, memory, temperature
- 📊 **OTel Native** — Standard OTLP export pipeline
- 🖥️ **Multi-GPU** — All devices on the node
- 📈 **Prometheus** — Built-in Prometheus exporter

**Tech:** Go · OpenTelemetry Collector SDK · NVML

</td>
</tr>
<tr>
<td width="50%">

### 🐳 [Docker GPU Dashboard Extension](https://github.com/pmady/docker-gpu-dashboard-extension)

[![Stars](https://img.shields.io/github/stars/pmady/docker-gpu-dashboard-extension?style=social)](https://github.com/pmady/docker-gpu-dashboard-extension)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**Real-time NVIDIA GPU metrics in Docker Desktop**

- 📊 **Live Dashboard** — Utilization, memory, temperature, power
- 📈 **History Charts** — 2-minute rolling Recharts graphs
- 🚦 **Alert Thresholds** — Color-coded green/yellow/red
- 🎭 **Mock Mode** — Develop without GPU hardware

**Tech:** Go · React · Recharts · Docker Extension SDK · NVML

</td>
<td width="50%">

### 🧠 [Kube Topology Agent](https://github.com/pmady/kube-topology-agent)

[![Stars](https://img.shields.io/github/stars/pmady/kube-topology-agent?style=social)](https://github.com/pmady/kube-topology-agent)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**K8s knowledge graph & automated root-cause analysis**

- 🗺️ **Knowledge Graph** — Real-time resource topology
- 🔍 **Root-Cause Traversal** — Graph-based incident investigation
- 🎮 **GPU Aware** — Training/inference/batch classification
- 🔔 **AlertManager** — Webhook integration for auto-investigation

**Tech:** Go · Kubernetes API · Gorilla Mux · Helm

</td>
</tr>
</table>

<p align="center">
  <b>More projects:</b> <a href="https://github.com/pmady/kubeai-autoscaler">KubeAI Autoscaler</a> · <a href="https://github.com/pmady/ingress2gateway">Ingress2Gateway</a> · <a href="https://github.com/pmady/golden-kubestronaut-learning">Golden Kubestronaut Learning</a> · <a href="https://github.com/pmady/llmops">LLMOps</a>
</p>

---

## 🌱 Open Source Contributions

> 31+ PRs across 17 projects in CNCF, ASWF, and open-source foundations.

### CNCF (Cloud Native Computing Foundation)

| Project | Description | Contributions |
|---------|-------------|---------------|
| **[Dragonfly](https://github.com/dragonflyoss)** | P2P-based file distribution and image acceleration | [client#1861](https://github.com/dragonflyoss/client/pull/1861) - Fix error chain propagation in backend stream failures, [client#1665](https://github.com/dragonflyoss/client/pull/1665) - Add Hugging Face backend support with hf:// protocol, [client#1673](https://github.com/dragonflyoss/client/pull/1673) - Add ModelScope backend support with modelscope:// protocol, [d7y.io#386](https://github.com/dragonflyoss/d7y.io/pull/386) - Add hf:// protocol documentation, [d7y.io#398](https://github.com/dragonflyoss/d7y.io/pull/398) - Add P2P-accelerated AI model downloads blog post, [helm-charts#455](https://github.com/dragonflyoss/helm-charts/pull/455) - Add injector support to helm chart, [helm-charts#480](https://github.com/dragonflyoss/helm-charts/pull/480) - Replace deprecated bitnamilegacy/mysql with bitnami/mysql |
| **[Kubernetes](https://github.com/kubernetes/website)** | Production-Grade Container Orchestration | [#53891](https://github.com/kubernetes/website/pull/53891) - Document deployment.kubernetes.io/* annotations, [#53892](https://github.com/kubernetes/website/pull/53892) - Add kubectl apply view-last-applied documentation |
| **[TiKV](https://github.com/tikv/tikv)** | Distributed transactional key-value database | [#19225](https://github.com/tikv/tikv/pull/19225) - Add AGENTS.md for AI agent guidance |
| **[Volcano](https://github.com/volcano-sh/volcano)** | Cloud-native batch scheduling for AI/HPC | [#5328](https://github.com/volcano-sh/volcano/pull/5328) - Fix typos in scheduler comments, [#5095](https://github.com/volcano-sh/volcano/pull/5095) - GPU NUMA topology awareness in scheduler, [apis#229](https://github.com/volcano-sh/apis/pull/229) - Add GPUInfo type to NumatopoSpec CRD, [resource-exporter#12](https://github.com/volcano-sh/resource-exporter/pull/12) - GPU NUMA topology discovery via sysfs |
| **[HAMi](https://github.com/Project-HAMi/HAMi)** | Heterogeneous AI Computing Virtualization Middleware | [#1893](https://github.com/Project-HAMi/HAMi/pull/1893) - Add unit tests for nvinternal info, mig, and watch packages |
| **[KEDA](https://github.com/kedacore/keda)** | Kubernetes Event-driven Autoscaling | [keda-docs#1658](https://github.com/kedacore/keda-docs/pull/1658) - Removing metricName from the kedadocs, [keda-docs#1769](https://github.com/kedacore/keda-docs/pull/1769) - Fix datadog scaler typos across all versions, [#7538](https://github.com/kedacore/keda/issues/7538) - GPU/AI inference scaler architectural analysis |
| **[Metal³](https://github.com/metal3-io/metal3-docs)** | Bare metal host provisioning for Kubernetes | [#624](https://github.com/metal3-io/metal3-docs/pull/624) - Fix redirect links in tryit.md |
| **[OpenTelemetry](https://github.com/open-telemetry/opentelemetry.io)** | Observability framework | [#8632](https://github.com/open-telemetry/opentelemetry.io/pull/8632) - Add .NET troubleshooting page |
| **[kpt](https://github.com/kptdev/kpt)** | Kubernetes-native packaging and resource management | [#4278](https://github.com/kptdev/kpt/pull/4278) - Fix kpt fn doc command for KRM functions expecting input |
| **[traceAI](https://github.com/future-agi/traceAI)** | Open-source LLM observability SDK | [#165](https://github.com/future-agi/traceAI/pull/165) - Fix exporter shutdown and thread safety in Python SDK, [#166](https://github.com/future-agi/traceAI/pull/166) - Add Go SDK with OpenAI instrumentor |

### ASWF (Academy Software Foundation)

| Project | Description | Contributions |
|---------|-------------|---------------|
| **[OpenColorIO](https://github.com/AcademySoftwareFoundation/OpenColorIO)** | Color management library | [#2229](https://github.com/AcademySoftwareFoundation/OpenColorIO/pull/2229) - Add release signing workflow, [#2230](https://github.com/AcademySoftwareFoundation/OpenColorIO/pull/2230) - Add Dependabot configuration, [#2243](https://github.com/AcademySoftwareFoundation/OpenColorIO/pull/2243) - Add Vulkan unit test framework |
| **[OpenCue](https://github.com/AcademySoftwareFoundation/OpenCue)** | Cloud rendering management system | [#2134](https://github.com/AcademySoftwareFoundation/OpenCue/pull/2134) - Add scheduled subscription recalculation task |
| **[OpenImageIO](https://github.com/AcademySoftwareFoundation/OpenImageIO)** | Image processing library | [#4976](https://github.com/AcademySoftwareFoundation/OpenImageIO/pull/4976) - Fix IBA::compare_Yee() channel access |
| **[RAWtoACES](https://github.com/AcademySoftwareFoundation/rawtoaces)** | RAW to ACES image conversion | [#222](https://github.com/AcademySoftwareFoundation/rawtoaces/pull/222) - Add build developer documentation |
| **[xSTUDIO](https://github.com/AcademySoftwareFoundation/xstudio)** | Playback and review application | [#186](https://github.com/AcademySoftwareFoundation/xstudio/pull/186) - Fix broken build guide links |

---

## 🧰 Tech Stack

<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=kubernetes,aws,azure,docker,go,prometheus,grafana,githubactions,terraform&perline=9" />
  </a>
</p>

<p align="left">
  <img src="https://img.shields.io/badge/KEDA-326CE5?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/ArgoCD-EF7B4D?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/Crossplane-1572B6?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/Helm-0F1689?style=flat&logo=helm&logoColor=white" />
  <img src="https://img.shields.io/badge/Volcano-326CE5?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/HAMi-FF6B35?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenTelemetry-425CC7?style=flat&logo=opentelemetry&logoColor=white" />
  <img src="https://img.shields.io/badge/Kyverno-326CE5?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/OPA-7D3C98?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/Flux-5468FF?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/Splunk-000000?style=flat&logo=splunk&logoColor=white" />
  <img src="https://img.shields.io/badge/Datadog-632CA6?style=flat&logo=datadog&logoColor=white" />
  <img src="https://img.shields.io/badge/NVIDIA_NVML-76B900?style=flat&logo=nvidia&logoColor=white" />
  <img src="https://img.shields.io/badge/gRPC-244C5A?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/Jenkins-D24939?style=flat&logo=jenkins&logoColor=white" />
  <img src="https://img.shields.io/badge/PrestoDB-5890FF?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/Trino-DD00A1?style=flat&logoColor=white" />
</p>

---
## �� GitHub Stats

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=pmady&show_icons=true&include_all_commits=true&count_private=true&theme=github_dark&rank_icon=github)](https://github.com/pmady)

*Stats updated on 2026-06-11 15:25 UTC*
## 🐍 Contribution Activity

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=pmady&theme=tokyo-night&hide_border=true&area=true&area_color=00B4D8&color=00B4D8&line=00B4D8&point=FFFFFF" width="100%" />
</p>

---

## 🤝 Let's Connect

<p align="center">
  Building GPU infrastructure for Kubernetes? Working on CNCF projects? Let's collaborate.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/pavanmadduri/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://medium.com/@pavan4devops">
    <img src="https://img.shields.io/badge/Medium-Follow-000000?style=for-the-badge&logo=medium&logoColor=white" />
  </a>
  <a href="https://github.com/pmady?tab=followers">
    <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%" />
