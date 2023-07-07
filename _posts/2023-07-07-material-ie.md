---
title: 'Extracting Information from Material Science Articles'
date: 2023-07-07
permalink: /posts/2023/07/material-ie/
toc: true
tags:
  - Information Extraction
  - Material Science
---

This article briefly introduces my work on information extraction from material science articles, which is decided to not be published as a serious conference/journal paper due to quality concerns (*i.e.*, insufficient innovation/impact).
But I figure it would be helpful to make it partly available to everyone in case it might be helpful or inspiring to someone who's doing similar work.
The code is available in [this GitHub repo](https://github.com/Yinghao-Li/MaterialPropertyExtractor).

**Disclaimer**: No content contributed by the collaborators of the original paper is included in this article.

## Abstract
Machine learning models can significantly accelerate polymer design by providing reliable predictions for material properties without the need for wet lab experiments.
However, manually constructing large-scale annotated datasets to train such models can be prohibitively difficult and time-consuming.
Although efforts have been made to develop Natural Language Processing (NLP) techniques for extracting information from literature data, these models usually require a significant amount of annotated data to train the extraction models effectively.
We propose an active learning-based model learning scheme that minimizes human effort in the information extraction pipeline.
We start with simple labeling rules to collect an initial set of noisy labels, a subset of which are then presented to material science experts to correct labeling mistakes.
Using this small set of labels, we train an information extraction model that extracts more data for collection and refinement, which is repeated over the candidate data points.
This active learning scheme significantly reduces human effort, as judging the correctness of an annotation is much more efficient than searching for entities in articles.
Experiments on ring-opening polymer property extraction show that our pipeline in total contributes 58 new data points to the property prediction dataset within half of the time for people to annotate from scratch without the assistance of our information extraction model.
The new data points are proven effective in reducing the enthalpy prediction error by 2.94 root mean square error of a machine learning model.

## Introduction

In recent years, there has been a remarkable advancement in material science technologies, leading to an explosion of experimental results on various types of materials.
Moreover, advanced machine learning (ML) models have emerged as promising tools for material science experts to estimate the properties of new materials directly.
These models can also aid in the design of wet lab experiments to accelerate the verification of predicted properties.
However, the construction of reliable ML models requires a sufficiently large training dataset, which can be challenging to acquire due to the scattering of relevant data points across numerous published literature.
Building such a dataset demands a considerable amount of work for locating informative papers and sentences, which is prohibitively challenging and time-consuming.

ML-based information extraction (IE) techniques have been developed by researchers to automatically locate relevant entities and elements within documents.
These techniques are adapted and customized to fit the material science domain.
IE techniques enable the processing of a large number of candidate documents in a short time, extracting the desired polymer property mentions while discarding irrelevant documents with relatively high precision.
Such approaches significantly improve workflow efficiency and facilitate the discovery of easily-overlooked information hidden in the corners of papers.
However, ML-based IE models used in previous works suffer from the same limitation as other supervised ML approaches, i.e., they require large-scale manually labeled datasets to achieve high performance.
The lack of such data is the very reason why IE methods are used in the first place.
One workaround is weak supervision, which employs dictionary matching or multiple simple heuristic rules to generate weak labels before aggregating and denoising them into one label set with unsupervised methods such as hidden Markov models.
Although weak supervision approaches have shown promising performance in denoising noisy input labels, they still cannot fully address the gap caused by annotation quality.
While labeling functions are quicker to construct initially, the marginal revenue from labeling new data points exceeds that from designing new labeling functions after several iterations of label annotation/labeling function application.

![ The pipeline of human-assisted information extraction pipeline from material science papers. ]({{base_path}}/images/material-ie/pipeline.png){#fig:1.pipeline width="95%"}

We propose an IE pipeline based on the active learning schema, as shown in Figure [1](#fig:1.pipeline){reference-type="ref" reference="fig:1.pipeline"}, to minimize human annotation effort without compromising model performance.
Similar to weak supervision approaches, we begin with simple labeling functions to provide an initial set of weakly annotated labels.
Rather than training models directly with these weak labels, we select a small subset of the annotated data and present them to human annotators for correction.
An ML model is then trained on the refined subset and applied to the article corpus to gather more data points with higher precision.
The annotation-training cycle is repeated several times until the supervised model no longer improves significantly with an increasing amount of training data.
Compared with annotating from scratch, correcting labels is an easier and more efficient task for human annotators as the range of input sentences is limited.
The active learning pipeline significantly reduces the human effort required to obtain results with comparable performance.

In previous research, data extraction from article abstracts, which often contain key information of interest, has been the focus due to their simplified format and availability on publisher websites.
However, the limited nature of abstracts means that they may not capture the detailed discussions necessary for material property extraction.
Other work in the inorganic materials domain has attempted to extract specific properties from the body of the paper using a rules-based parser such as the ChemDataExtractor framework.
In our work, we propose to expand the extraction pipeline to include the article bodies, which requires the development of a custom article parser to maintain the semantic and structural information in the original paper.
Rather than using off-the-shelf parsers, we create a parser tailored for each publisher to ensure cleaner parsing results, and our experiments show the superiority of this approach in case studies.

To demonstrate the effectiveness of our proposed pipeline, we evaluate its performance in extracting thermodynamic data related to ring-opening polymerization (ROP).
ROP is a reaction that creates polymers from cyclic monomers and is of particular interest to the polymer science community due to the potential for developing chemically recyclable polymers.
The development of such polymers is crucial in addressing the global plastic waste crisis.
Moreover, the chemical space of ROP-derived polymers is vast, offering flexibility to discover polymers that are both chemically recyclable and mechanically robust enough to replace commodity plastics.
Specifically, the proposed IE pipeline is used to extract the enthalpy and entropy of polymerization, as well as the ceiling temperature ($\Delta H$, $\Delta S$, and $T_{c}$ respectively) of ROP polymer materials.
These properties were selected as they are essential for determining the chemical respectability of ROP polymers.
Focusing on ROP polymers also presents a challenging and specific IE task, as thermodynamic data from other polymerization types can appear similar in sentences, and there is limited available data in the literature.
Therefore, by applying to extract thermodynamic data for ROP, the IE pipeline can be well validated, performance metrics can be captured, and data for creating ML models to screen polymers for chemical recyclability can be extracted for future use.

In summary, our contribution is threefold:
1.  we develop an advanced material science paper parser that leads to more accurate parsing results and better content coverage;

2.  we propose an active learning-based information extraction pipeline that achieves promising performance with minimal human involvement; and

3.  we validate our system on the specific task of identifying thermodynamic properties within the scientific literature and demonstrate the effectiveness of our system in providing valuable data for the development of machine learning models to screen polymers for chemical recyclability.
