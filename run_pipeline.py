import pandas as pd
import ollama

# -----------------------------
# Configuration
# -----------------------------
MODEL_1 = "llama3:latest"
MODEL_2 = "llama3.1:latest"
INPUT_FILE = "prompts.csv"
OUTPUT_FILE = "results.csv"

# -----------------------------
# Load CSV prompt dataset
# -----------------------------
try:
    df = pd.read_csv(INPUT_FILE, sep="\t")  
    df.columns = df.columns.str.strip().str.lower()
except FileNotFoundError:
    print(f"Error: {INPUT_FILE} not found.")
    exit()

results = []

print(f"Starting pipeline using {MODEL_1} and {MODEL_2}...")

# -----------------------------
# Process each prompt
# -----------------------------
for idx, row in df.iterrows():
    question = row["prompt"]
    print(f"Processing Prompt {idx}...")

    # 1. Llama 3 generates the initial response
    # We use .generate for a simple text completion or .chat for conversation
    response_1 = ollama.chat(model=MODEL_1, messages=[
        {'role': 'user', 'content': question}
    ])
    llama3_output = response_1['message']['content']

    # 2. Llama 3.1 evaluates the Llama 3 response
    evaluation_prompt = f"""You are an expert AI evaluator. 
Your task is to refine or verify the output of an older model (Llama 3).

USER QUESTION: {question}

LLAMA 3 RESPONSE: {llama3_output}

ANALYSIS: Analyze if the response is correct. If it is wrong or incomplete, explain why and provide a better response."""

    response_2 = ollama.chat(model=MODEL_2, messages=[
        {'role': 'user', 'content': evaluation_prompt}
    ])
    llama3_1_output = response_2['message']['content']

    # Store results
    results.append({
        "prompt_id": idx,
        "prompt": question,
        "llama3_response": llama3_output,
        "llama3_1_evaluation": llama3_1_output
    })

# -----------------------------
# Save results
# -----------------------------
output_df = pd.DataFrame(results)
output_df.to_csv(OUTPUT_FILE, index=False)

print(f"\nPipeline execution complete. Results saved to {OUTPUT_FILE}")
