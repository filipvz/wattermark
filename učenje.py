import streamlit as st
from PIL import Image, ImageDraw,ImageFont
import io

# Početak

st.title(" Watermark Alat")
st.write("Powered by Filip (20% Digital)")
st.write("Upload your image for watermarking.")

korisnikov_tekst=st.text_input("Enter your watermark text:")
učitana_datoteka = st.file_uploader("Upload your image...", type=["jpg", "jpeg", "png"],accept_multiple_files=True)


if učitana_datoteka:
    #Korisnikova slika
    st.write(f"Proccessing {len(učitana_datoteka)} images...")
    prozirnost=st.slider("Your Watermark visibility: ",0,255,128)
    for slika_fajl in učitana_datoteka:
        
     img = Image.open(slika_fajl).convert("RGBA")
     tekst_sloj=Image.new("RGBA",img.size,(255,255,255,0))
     crtaj = ImageDraw.Draw(tekst_sloj)
     sirina,visina=img.size


    
     try:
          font=ImageFont.truetype("arial.ttf",80)
     except:
          font=ImageFont.load_default()
     lijevo,gore,desno,dolje=crtaj.textbbox((0,0),korisnikov_tekst,font=font)
     sirina_teksta=desno-lijevo
     visina_teksta=dolje-gore
            
     pozicija = (sirina - sirina_teksta-50, visina -visina_teksta -50)
    
     crtaj.text(pozicija, korisnikov_tekst, fill=(255, 255, 255,prozirnost),font=font)
     img=Image.alpha_composite(img,tekst_sloj)
     finalna_slika=img.convert("RGB")
    
     st.divider()
     st.image(finalna_slika, caption=f"Processed: {slika_fajl.name}")
    
     buf=io.BytesIO()
     finalna_slika.save(buf,format="JPEG")
     st.download_button(
            label=f"Download {slika_fajl.name}",
            data=buf.getvalue(),
            file_name=f"watermarked_{slika_fajl.name}",
            key=f"download_{slika_fajl.name}"
        
    )

    st.write("Thanx for using our app!")

    

