import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('example.csv')

df['ingreso_total'] = df['cantidad'] * df['precio_unitario']

print("--- Registro de Ventas con Ingreso Calculado ---")
print(df.head(7))

ventas_por_categoria = df.groupby('categoria')['ingreso_total'].sum().sort_values(ascending=False)

print("\n--- Ingresos Totales por Categoría ---")
print(ventas_por_categoria)

ventas_paypal = df[df['metodo_pago'] == 'PayPal']

print("\n--- Transacciones pagadas con PayPal ---")
print(ventas_paypal[['fecha', 'producto', 'ingreso_total']])

ventas_por_categoria.plot(kind='bar', color='coral', edgecolor='black')

plt.title('Ingresos Totales por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Dinero Ingresado ($)')
plt.xticks(rotation=45) # Gira los textos para que se lean mejor
plt.tight_layout() # Ajusta los márgenes
plt.show() # Esta línea abre una ventana con tu gráfico