import streamlit as st
import pandas as pd

from dataset_engine.profiler import profile_dataset
from dslm.task_identifier import identify_task
from workflow.workflow_generator import generate_workflow

st.title("CortexFlow AI")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.write(df.head())

    profile = profile_dataset(df)

    st.subheader("Dataset Profile")
    st.json(profile)

    task = identify_task(df)

    st.subheader("Detected Task")
    st.success(task)

    workflow = generate_workflow(task)

    st.subheader("Generated Workflow")

    for step in workflow:
        st.write("➡", step)
