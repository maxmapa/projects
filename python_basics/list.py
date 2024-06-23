names: list[str] = ['James', 'Charlotte', 'Stephany', 'Mario', 'Sandra']
long_names: list[str] = [name for name in names if len(name) > 7]
print(f'Long names: {long_names}')