# Importar a biblioteca pandas
import pandas as pd

# Função para salvar as informações da ferramenta
def save_info():
    tool_code = tool_code_entry.get()
    request_description = request_description_entry.get()
    checkout_date = checkout_date_entry.get()
    checkout_time = checkout_time_entry.get()
    return_date = return_date_entry.get()
    return_time = return_time_entry.get()
    
    # Criar um dicionário com as informações
    data = {"Código da Ferramenta": [tool_code], 
            "Descrição da Solicitação": [request_description],
            "Data de Retirada": [checkout_date],
            "Hora de Retirada": [checkout_time],
            "Data de Devolução Prevista": [return_date],
            "Hora de Devolução Prevista": [return_time]}
    
    # Converter o dicionário em um DataFrame
    df = pd.DataFrame(data)
    
    # Salvar o DataFrame em um arquivo Excel
    df.to_excel("informacoes_ferramenta.xlsx", index=False)
    
    messagebox.showinfo("Informações salvas", f"Ferramenta: {tool_code}\nDescrição: {request_description}\nData de retirada: {checkout_date} às {checkout_time}\nData de devolução prevista: {return_date} às {return_time}")
