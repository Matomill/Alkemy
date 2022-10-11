import pandas as pd
import download_data


library_path= filename(category3)
museos_path= filename(category1)
teatros_path= filename(category2)

# Creating a list in order to normalize headers
headers= ['cod_localidad','id_provincia','id_departamento','categoría','provincia','localidad','nombre','domicilio','código postal',
          'número de teléfono','mail','web']

# Creating a unique table
df_library= pd.read_csv(library_path)
df_library2= df_library[['Cod_Loc','IdProvincia','IdDepartamento','Categoría','Provincia','Localidad','Nombre','Domicilio'
    ,'CP','Teléfono','Mail','Web']]
df_library2.columns= headers


df_museos= pd.read_csv(museos_path)
df_museos2= df_museos[['Cod_Loc','IdProvincia','IdDepartamento','categoria','provincia','localidad','nombre','direccion','CP','telefono','Mail','Web']]
df_museos2.columns= headers

df_teatros= pd.read_csv(teatros_path)
df_teatros2= df_teatros[['cod_loc','id_prov','id_departamento','categoria','provincia','localidad','nombre','domicilio','CP','telefono','mail','web']]
df_teatros2.columns= headers

df_unique= pd.concat([df_library2, df_museos2, df_teatros2])

# processing unique table
df_library3= df_library[['Categoría','Fuente','Provincia','Nombre']]
df_museos3= df_museos[['categoria','fuente','provincia','nombre']].rename(columns={'categoria':'Categoría','fuente':'Fuente','provincia':'Provincia','nomber':'Nombre'})
df_teatros3= df_teatros[['categoria','fuente','provincia','nombre']].rename(columns={'categoria':'Categoría','fuente':'Fuente','provincia':'Provincia','nomber':'Nombre'})
df_datos_conjuntos= pd.concat([df_library3, df_museos3, df_teatros3])

# Normaliziong unique table

df_datos_conjuntos['Provincia'] = df_datos_conjuntos['Provincia'].replace({'Ciudad Autonoma de Buenos Aires':'Ciudad Autónoma de Buenos Aires',
                                                              'Entre Rios':'Entre Ríos',
                                                              'Neuquen':'Neuquén',
                                                              'Neuquén\xa0':'Neuquén',
                                                              'Rio Negro':'Río Negro',
                                                              'Santa Fe':'Santa Fé',
                                                              'Tierra del Fuego':'Tierra del Fuego, Antártida e Islas del Atlántico Sur',
                                                              'Tucuman':'Tucumán'})

# Creating table of number of records per category

df_total_cat= df_datos_conjuntos.pivot_table(index=['Categoría'], values='Nombre', margins=True, aggfunc=len)
df_total_fuente= df_datos_conjuntos.pivot_table(index=['Provincia'], values='Nombre', margins=True, aggfunc=len)
df_total_prov_cat= df_datos_conjuntos.pivot_table(index=['Provincia','Categoría'], values='Nombre', margins=True, aggfunc=len)

# Working with Teatro data. Cine information was not longer available.


teatros_norm = df_teatros[['provincia', 'capacidad']]
teatros_norm = teatros_norm['provincia'].replace({'Ciudad Autonoma de Buenos Aires':'Ciudad Autónoma de Buenos Aires',
                                                              'Entre Rios':'Entre Ríos',
                                                              'Neuquen':'Neuquén',
                                                              'Neuquén\xa0':'Neuquén',
                                                              'Rio Negro':'Río Negro',
                                                              'Santa Fe':'Santa Fé',
                                                              'Tierra del Fuego':'Tierra del Fuego, Antártida e Islas del Atlántico Sur',
                                                              'Tucuman':'Tucumán'})

# Normalizing teatro data
teatros_norm['capacidad'] = teatros_norm['capacidad'].fillna(0)
teatros_norm['capacidad'] = teatros_norm['capacidad'].astype('int')
teatros_norm['capacidad'] = teatros_norm['capacidad'].replace(0, teatros_norm['capacidad'].mean())
teatros_norm = teatros_norm.groupby('provincia').sum()
