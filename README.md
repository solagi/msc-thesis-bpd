# MSc Thesis - Assessing Bipolar Disorder Using Neural Networks

**Authors**: Agita Solzemniece and Anuchit James Herskov  
<!-- **Supervisors**: Stella Grasshof and Sami Brandt  
 -->
**Sumbitted**: May, 2022

Source code for Master thesis developed by MSc Software Design students of IT University of Copenhagen. 
The repository does not contain the dataset used for this research due to the privacy agreement.

# Abstract

This study examines how the severity of Bipolar Disorder (BPD) can be assessed using neural networks (NN) with visual and audio modalities as input. Both modalities are represented through low-level-descriptors (LLDs) from recordings extracted from interviewed subjects under The Turkish Audio-Visual Bipolar Disorder Corpus 2018. For this research, two NN architectures are proposed and examined for the problem domain - Long-Short-Term Memory (LSTM) network and Temporal Convolutional network (TCN). The output of the models represents the severity of a subject’s BPD state, which has been assessed with the Young Mania Rating Scale (YMRS). The LSTM and TCN architectures have proven to
be effective in working with sequence related tasks, due to their ability to handle long-range dependencies and deal with the vanishing or exploding gradient problem. As such, both architectures are good candidates for working with the sequential format of video and audio data. Although most tasks within the domain of mental illness diagnostics tend to be defined as classification problems, this research attempts to contribute to the field in the form of a regression task. Development and conclusions of this research acknowledge the complexity of the BPD nature and assessing its severity by regression task, as the performance of both NN models results in high tendency to overestimate the YMRS score for BPD subjects for all three data modalities.
