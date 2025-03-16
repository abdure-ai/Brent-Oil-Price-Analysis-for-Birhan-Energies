{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-03-16 00:07:16.633 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-16 00:07:17.117 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run c:\\Users\\user\\Projects\\Brent-Oil-Price-Analysis-for-Birhan-Energies\\.venv\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-03-16 00:07:17.120 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-16 00:07:25.049 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-16 00:07:25.050 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-16 00:07:25.052 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-16 00:07:25.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-16 00:07:25.054 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-16 00:07:25.055 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-16 00:07:25.056 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-16 00:07:25.057 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-16 00:07:25.155 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-16 00:07:25.156 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "\n",
    "# Load data\n",
    "df = pd.read_csv(r\"C:\\Users\\user\\Projects\\Brent-Oil-Price-Analysis-for-Birhan-Energies\\data\\proecessed\\cleaned_brent_oil.csv\")\n",
    "\n",
    "st.title(\"Brent Oil Price Analysis Dashboard\")\n",
    "\n",
    "# Line chart for price trends\n",
    "fig = px.line(df, x='Date', y='Price', title=\"Brent Oil Prices Over Time\")\n",
    "st.plotly_chart(fig)\n",
    "\n",
    "st.write(\"### Summary Statistics\")\n",
    "st.write(df.describe())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
