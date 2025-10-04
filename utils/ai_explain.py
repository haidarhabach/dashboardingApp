import openai
import pandas as pd


def explain_chart(chart_type : str ,df:pd.DataFrame,column:str,api_key:str):
    try:
        #3ashen ne5od statistics informations metel mean,count,...
        stats=df[column].describe().to_dict()
        #na3rf range el ma3loumet la n7asen prompt el ai
        data_range = f"{df[column].min()} to {df[column].max()}"
        #la nshouf kam null value fi kmn 3ashen n7asen jaweb el ai
        missing_count=df[column].isnull().sum()

        #el resele li r7 tenba3at lal ai
        prompt=f"""
            Analyze this {chart_type} and provide a comprehensive description. Include:
            1. Chart type and purpose
            2. Key trends and patterns
            3. Notable data points
            4. Insights and observations
            5. Any limitations or considerations
        
            Chart type: {chart_type}
            Column analyzed: {column}
            Data statistics: {stats}
            Data range: {data_range}
            Missing values: {missing_count}
            Total observations: {len(df)}
        
            Provide a clear, professional description:
            """
        #na3te lal ai el api key
        client = openai.OpenAI(api_key=api_key) if api_key else openai.OpenAI()

        #neb3at el prompt
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}],
            max_tokens=500,#n7ot limit la toul el jaweb
            temperature=0.3 #kel ma a2al el jaweb bkoun a7sa
        )
        #n3ml return lal jaweb
        return response.choices[0].message.content
    
    except Exception as e:
        #handling errors
        return f"Error generating explanation: {str(e)}"