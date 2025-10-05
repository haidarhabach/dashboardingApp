import pandas as pd
import matplotlib.pyplot as plt

def visualize_file(file_path):
    try:
        # Try reading as CSV  or  text
        try:
            data = pd.read_csv(file_path, header=None)
        except Exception:
            data = pd.read_table(file_path, header=None)
        
        values = data[0].dropna().tolist()
        # Check if numeric or string
        if all(str(v).strip().isdigit() for v in values):
            # Convert into  integers
            values = list(map(int, values))
            
            # group values and count occurrences
            grouped = pd.Series(values).value_counts().sort_index()

            # Draw pie chart
            plt.figure(figsize=(6,6))
            grouped.plot.pie(
                autopct='%1.1f%%', 
                startangle=90, 
                shadow=True,
                colormap='coolwarm'
            )
            plt.title("Pie Chart of Integer Data (Optimized)")
            plt.ylabel('')
            plt.show()

        else:
            #clean and group text data
            clean_values = [str(v).strip().capitalize() for v in values]
            # pcik the first 10 (a5dna awl 10)
            grouped = pd.Series(clean_values).value_counts().head(10)  

            # Draw bar chart if not integer
            plt.figure(figsize=(8,5))
            grouped.plot.bar(
                color='skyblue',
                edgecolor='black'
            )
            plt.title("Bar Chart of String Data (Optimized)")
            plt.xlabel("Category")
            plt.ylabel("Frequency")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    except Exception as e:
        print(f"the Error is : {e}")

# Example
# visualize_file("test.txt")
# visualize_file("test.csv")

