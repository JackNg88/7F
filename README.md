# JMMG-NES Reprogramming: Induction of Pluripotent Stem Cells from Mouse Embryonic Fibroblasts (MEFs)

This repository contains **figures, scripts, and data analyses** related to our study on the induction of pluripotent stem cells (iPSCs) from mouse embryonic fibroblasts using the JMMG-NES combination: **Jdp2, Jhdm1b, Mkk6, Glis1, Nanog, Essrb, Sall4**.

---

## Project Overview

The goal of this project is to explore efficient reprogramming of MEFs into iPSCs using a defined set of transcription factors and epigenetic regulators. This repository provides:

- Scripts for data processing, analysis, and figure generation  
- Figures for manuscript preparation  
- Supplementary analyses for gene expression, chromatin accessibility, and trajectory inference  

Our analyses focus on single-cell and bulk RNA-seq, ATAC-seq, and integrative multi-omics approaches to characterize transcriptional and epigenetic dynamics during reprogramming.

---

## Repository Structure

JMMG-NES_project/
├── README.md                  # Project description
├── figures/                   # Generated figures for publication and analysis
├── scripts/                   # Analysis scripts (R, Python)
│   ├── scRNAseq_analysis.R
│   ├── trajectory_inference.R
│   └── figure_generation.py
├── data/                      # Raw and processed data (optional)
├── results/                   # Outputs and intermediate files
└── docs/                      # Additional notes or documentation

---

## Getting Started

1. Clone this repository:
```bash
git clone https://github.com/YourUsername/JMMG-NES_project.git

	2.	Install required packages:

# R example
install.packages(c("Seurat", "ggplot2", "dplyr", "Monocle3"))

# Python example
pip install pandas matplotlib scanpy anndata

	3.	Run scripts in the scripts/ folder to reproduce figures and analyses.

⸻

Key Computational Analyses
	•	Single-cell RNA-seq: preprocessing, clustering, marker identification, pseudotime and trajectory inference
	•	Chromatin accessibility (ATAC-seq): peak calling, annotation, and integration with transcriptional data
	•	Gene regulatory network reconstruction: identifying factor-driven transcriptional programs
	•	Figure generation: high-quality figures for publication and supplementary materials

These analyses were designed to reproduce and extend the findings of the JMMG-NES-mediated iPSC induction study, providing computational pipelines for transcriptomic and epigenetic data.

⸻

Reference

Bo Wang, Linlin Wu, Dongwei Li, et al. Induction of Pluripotent Stem Cells from Mouse Embryonic Fibroblasts by Jdp2-Jhdm1b-Mkk6-Glis1-Nanog-Essrb-Sall4.
Cell Rep. 2019 Jun 18;27(12):3473-3485.e5.
DOI: 10.1016/j.celrep.2019.05.068￼
PMID: 31216469

⸻

License

This repository is licensed under the MIT License.
Scripts and figures can be freely used for research purposes with proper citation of this project and the original publication.

---

Contact

If you have any questions, issues, or suggestions regarding this repository,  
please feel free to contact:

**Jian Wu**  
📧 Email: Jian.Wu@mpi-bn.mpg.de

---
