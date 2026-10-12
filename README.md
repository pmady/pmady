# Pavan Madduri

<img src="https://raw.githubusercontent.com/pmady/pmady/main/pavan-madduri-headshot.jpg" alt="Pavan Madduri" width="160" />

Senior cloud platform engineer working on GPU and AI infrastructure for Kubernetes.

- CNCF TAG Workloads Foundation Tech Lead (2026-2028)
- CNCF Golden Kubestronaut (KCNA, CKA, CKAD, CKS, KCSA)
- Oracle ACE Associate
- Dragonfly community member

[LinkedIn](https://www.linkedin.com/in/pavanmadduri/) · [Docker Hub](https://hub.docker.com/u/pmady7389)

## Projects

| Project | What it does |
|---|---|
| [keda-gpu-scaler](https://github.com/pmady/keda-gpu-scaler) | KEDA external scaler that reads NVIDIA GPU metrics from NVML on each node and scales vLLM, Triton and training workloads, including scale to zero. Go, gRPC, Helm. Referenced in [KEDA #7538](https://github.com/kedacore/keda/issues/7538). |
| [gpu-mcp-server](https://github.com/pmady/gpu-mcp-server) | NVIDIA GPU and MIG metrics as MCP tools for AI agents. Published on the [MCP Registry](https://registry.modelcontextprotocol.io). |
| [otel-gpu-receiver](https://github.com/pmady/otel-gpu-receiver) | OpenTelemetry Collector receiver for GPU metrics via NVML, with OTLP export and a Prometheus endpoint. |
| [docker-gpu-dashboard-extension](https://github.com/pmady/docker-gpu-dashboard-extension) | Docker Desktop extension showing live NVIDIA GPU utilization, memory, temperature and power. |
| [kube-topology-agent](https://github.com/pmady/kube-topology-agent) | Kubernetes resource knowledge graph with root-cause traversal and an AlertManager webhook. |
| [kubeai-autoscaler](https://github.com/pmady/kubeai-autoscaler), [ingress2gateway](https://github.com/pmady/ingress2gateway), [golden-kubestronaut-learning](https://github.com/pmady/golden-kubestronaut-learning), [llmops](https://github.com/pmady/llmops) | Smaller projects and learning material. |

## Upstream contributions

### CNCF

| Project | Pull requests |
|---|---|
| [Dragonfly](https://github.com/dragonflyoss) | [client#1861](https://github.com/dragonflyoss/client/pull/1861) fix error chain propagation in backend stream failures; [client#1665](https://github.com/dragonflyoss/client/pull/1665) Hugging Face backend (hf://); [client#1673](https://github.com/dragonflyoss/client/pull/1673) ModelScope backend (modelscope://); [d7y.io#386](https://github.com/dragonflyoss/d7y.io/pull/386) hf:// protocol docs; [d7y.io#398](https://github.com/dragonflyoss/d7y.io/pull/398) P2P model download blog post; [helm-charts#455](https://github.com/dragonflyoss/helm-charts/pull/455) injector support; [helm-charts#480](https://github.com/dragonflyoss/helm-charts/pull/480) replace deprecated bitnamilegacy/mysql |
| [Kubernetes](https://github.com/kubernetes/website) | [website#53891](https://github.com/kubernetes/website/pull/53891) document deployment.kubernetes.io/* annotations; [website#53892](https://github.com/kubernetes/website/pull/53892) kubectl apply view-last-applied docs |
| [TiKV](https://github.com/tikv/tikv) | [#19225](https://github.com/tikv/tikv/pull/19225) AGENTS.md for AI agent guidance |
| [Volcano](https://github.com/volcano-sh/volcano) | [#5095](https://github.com/volcano-sh/volcano/pull/5095) GPU NUMA topology awareness in the scheduler; [resource-exporter#12](https://github.com/volcano-sh/resource-exporter/pull/12) GPU NUMA topology discovery via sysfs; [apis#229](https://github.com/volcano-sh/apis/pull/229) GPUInfo type for NumatopoSpec; [#5328](https://github.com/volcano-sh/volcano/pull/5328) typo fixes |
| [HAMi](https://github.com/Project-HAMi/HAMi) | [#1893](https://github.com/Project-HAMi/HAMi/pull/1893) unit tests for nvinternal info, mig and watch packages |
| [KEDA](https://github.com/kedacore/keda) | [#7538](https://github.com/kedacore/keda/issues/7538) GPU scaler design discussion; [keda-docs#1658](https://github.com/kedacore/keda-docs/pull/1658) remove metricName from docs; [keda-docs#1769](https://github.com/kedacore/keda-docs/pull/1769) Datadog scaler typo fixes |
| [Metal³](https://github.com/metal3-io/metal3-docs) | [#624](https://github.com/metal3-io/metal3-docs/pull/624) fix redirect links in tryit.md |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry.io) | [#8632](https://github.com/open-telemetry/opentelemetry.io/pull/8632) .NET troubleshooting page |
| [kpt](https://github.com/kptdev/kpt) | [#4278](https://github.com/kptdev/kpt/pull/4278) fix kpt fn doc for KRM functions expecting input |
| [traceAI](https://github.com/future-agi/traceAI) | [#165](https://github.com/future-agi/traceAI/pull/165) exporter shutdown and thread safety in the Python SDK; [#166](https://github.com/future-agi/traceAI/pull/166) Go SDK with OpenAI instrumentor |

### Academy Software Foundation

| Project | Pull requests |
|---|---|
| [OpenColorIO](https://github.com/AcademySoftwareFoundation/OpenColorIO) | [#2229](https://github.com/AcademySoftwareFoundation/OpenColorIO/pull/2229) release signing workflow; [#2230](https://github.com/AcademySoftwareFoundation/OpenColorIO/pull/2230) Dependabot configuration; [#2243](https://github.com/AcademySoftwareFoundation/OpenColorIO/pull/2243) Vulkan unit test framework |
| [OpenCue](https://github.com/AcademySoftwareFoundation/OpenCue) | [#2134](https://github.com/AcademySoftwareFoundation/OpenCue/pull/2134) scheduled subscription recalculation task |
| [OpenImageIO](https://github.com/AcademySoftwareFoundation/OpenImageIO) | [#4976](https://github.com/AcademySoftwareFoundation/OpenImageIO/pull/4976) fix IBA::compare_Yee() channel access |
| [RAWtoACES](https://github.com/AcademySoftwareFoundation/rawtoaces) | [#222](https://github.com/AcademySoftwareFoundation/rawtoaces/pull/222) build and developer documentation |
| [xSTUDIO](https://github.com/AcademySoftwareFoundation/xstudio) | [#186](https://github.com/AcademySoftwareFoundation/xstudio/pull/186) fix broken build guide links |

## Tools I work with

Go, Kubernetes, KEDA, Volcano, HAMi, Helm, ArgoCD, Flux, Crossplane, OpenTelemetry, Prometheus, Grafana, NVIDIA NVML, gRPC, Terraform, GitHub Actions, AWS, Azure, OCI.
