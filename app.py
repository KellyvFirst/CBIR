import streamlit as st
import cv2,os,time #temps de chaque requête
import numpy as np
import glob
import matplotlib.pyplot as plt
from PIL import Image
from descriptors import bitdesc
import pandas as pd
from scipy.spatial import distance 
from distances import distance_selection
from upload import upload_file
def main():
    print("App launched !")
    input_value=st.sidebar.number_input("Enter a value",min_value=1,max_value=500,value=10,step=1)
    #Display input value
    st.sidebar.write(f"You enter{input_value}")
    #Define distances
    options =["Euclidean","Canberra","Manhattan","Chebyshev","Minkowsky"]
    selected_distance_option=st.sidebar.selectbox("Select a distance",options)
    st.sidebar.write(f"you chose {selected_distance_option}")
    # Import off-line database(signatures)
    signatures=np.load('cbir_signatures_v1.npy')
    #st.write(signatures)
    #Define a list for computed distances
    distanceList=list()
    #Upload Image
    is_image_uploaded=upload_file()
    if is_image_uploaded:
        st.write('''
                    # search Results
                ''')
       
         #Retrieve query image
        query_image='uploaded_images/query_image.png'
        #Read image as gray - scale
        img =cv2.imread(query_image,0)
        #Get signatures (extract features)of query image/compute Bitdesc
        bit_feat=bitdesc(img)
        # Compute and store  similarity distances
        for sign in signatures:
            # Remove the last two columns('subfolder','path') of the array
            sign = np.array(sign)[0:-2].astype('float')
            # Convert numpy array to list
            sign = sign.tolist()
            # Call distance function
            distances = distance_selection(selected_distance_option,bit_feat, sign)
            distanceList.append(distances)
            # print(f'Distance: {distance}')
        print('Distance computed Successfully!')
        #Compute n min distances
        minDistances=list()
        for i in range(input_value):
          array=np.array(distanceList)
          #Get index of min value from distance list and add to mindistances list
          index_min =np.argmin(array)
          minDistances.append(index_min)
          #Grab max value
          max=array.max()
          #OverWrite the min value with max value
          distanceList[index_min]=max
        print(minDistances)
        #Retrieve
        #image_paths=list()
        #for
        #
        image_paths=[signatures[small][-1] for small in minDistances]
        #
        classes=[signatures[small][-2] for small in minDistances]
        classes=np.array(classes)
        #Get unique values of
        unique_values,counts =np.unique(classes,return_counts=True)
        list_classes=list()
        print("unique Value with their counts")
        for value,count in zip(unique_values,counts):
            print(f"{value}:{count}")
            list_classes.append(value)
        #
        df=pd.DataFrame({"Value":unique_values,"frequency":counts})
        #
        #
        #st.bar_chart and set value as index,frequency
        st.bar_chart(df.set_index("Value"))
      


        #Display
        #Charger et afficher les images similaires
        # for i, path in enumerate(image_paths):
        #     st.write(f"Image similaire {i+1}:")
        #     image = Image.open(path)
        #     image = image.resize((200,200))
        #     st.image(image,caption=f"Image similaire {i+1}", use_column_width=True)
        
        num_columns = st.sidebar.number_input("Nombre de colonnes", min_value=1, max_value=5, value=3, step=1)
        # Diviser l'espace en colonnes
        columns = st.columns(num_columns)

        # Afficher les images dans les colonnes
        for i, path in enumerate(image_paths):
            #La fonction enumerate est une fonction intégrée de Python
            #  qui permet d'itérer sur une séquence (comme une liste ou un tuple) tout en conservant la trace de l'index de chaque élément dans la séquence.
            #  Elle renvoie une paire (index, élément) à chaque itération.
            with columns[i % num_columns]:
                st.write(f"Image similaire {i+1}:")
                image = Image.open(path)
                image = image.resize((200,200))
                st.image(image, caption=f"Image similaire {i+1}", use_column_width=True)

        

    else:
        st.write("Welcome! Please upload an image to get started...")



if __name__=="__main__":
    main()