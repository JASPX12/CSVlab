import pandas as pd

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