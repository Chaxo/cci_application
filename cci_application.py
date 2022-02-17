import streamlit as st
from streamlit.hashing import _CodeHasher
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server
import py_avataaars as pa
from PIL import Image
import base64
from random import randrange

# Here you can change the order and name
def main():
    state = _get_state()
    pages = {
            "Gender": page_gender,
            "1. Background": page_background,
            "2. Skin Color": page_skin_color,
            "3. Hairstyle/Hat": page_top_type,
            "4. Hair Color": page_hair_color,
            "5. Hat Color": page_hat_color,
            "6. Eyebrow Type": page_eyebrow_type,
            "7. Eye Type": page_eye_type,
            "8. Glasses": page_glasses_type,
            "9. Mouth": page_mouth_type,
            "10. Facial Hair Type": page_facial_hair_type,
            "11. Facial Hair Color": page_facial_hair_color,
            "12. Clothing": page_clothe_type,
            "13. Clothing Color": page_clothe_color,
            "14. Clothing Graphic": page_clothe_graphic,
            "15. Redirect to survey": page_redirect,
        }

    st.sidebar.title("Avatar Customization")
    page = st.sidebar.selectbox("There are 15 options available starting at step 0", tuple(pages.keys()))

     # Display the selected page with the session state
    pages[page](state)

    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    state.sync()


st.header ('Welcome to this avatar customization application')
st.write ("""Preview of the avatar and download option (PNG file) can be found below. Customization options can be found on the left side.""")
st.write("""Some avatar options are gender specific. An error could occur if such option is selected and the gender is changed. Please refrain from changing gender after leaving step 0 (Gender).
\n If you encounter any other errors, try selecting another option to resolve it. Otherwise, refresh the page.
 """)

# Changing Avatar List Names
# Background
pa.AvatarStyle.Circle = pa.AvatarStyle.CIRCLE
pa.AvatarStyle.Transparent = pa.AvatarStyle.TRANSPARENT
# Skin Color
pa.SkinColor.Black = pa.SkinColor.BLACK
pa.SkinColor.Tanned = pa.SkinColor.TANNED
pa.SkinColor.Yellow = pa.SkinColor.YELLOW
pa.SkinColor.Pale = pa.SkinColor.PALE
pa.SkinColor.Light = pa.SkinColor.LIGHT
pa.SkinColor.Brown = pa.SkinColor.BROWN
pa.SkinColor.Dark_Brown = pa.SkinColor.DARK_BROWN
# Hair Color
pa.HairColor.Black = pa.HairColor.BLACK
pa.HairColor.Auburn = pa.HairColor.AUBURN
pa.HairColor.Blonde = pa.HairColor.BLONDE
pa.HairColor.Blonde_Golden = pa.HairColor.BLONDE_GOLDEN
pa.HairColor.Brown = pa.HairColor.BROWN
pa.HairColor.Brown_Dark = pa.HairColor.BROWN_DARK
pa.HairColor.Pastel_Pink = pa.HairColor.PASTEL_PINK
pa.HairColor.Platinum = pa.HairColor.PLATINUM
pa.HairColor.Red = pa.HairColor.RED
pa.HairColor.Silver_Gray = pa.HairColor.SILVER_GRAY
# Facial Hair
pa.FacialHairType.Default = pa.FacialHairType.DEFAULT
pa.FacialHairType.Medium = pa.FacialHairType.BEARD_MEDIUM
pa.FacialHairType.Light = pa.FacialHairType.BEARD_LIGHT
pa.FacialHairType.Majestic = pa.FacialHairType.BEARD_MAJESTIC
pa.FacialHairType.Moustache_Fancy = pa.FacialHairType.MOUSTACHE_FANCY
pa.FacialHairType.Moustache_Magnum = pa.FacialHairType.MOUSTACHE_MAGNUM
# Facial Hair + Hat + Clothe Color
pa.ClotheColor.Black = pa.ClotheColor.BLACK
pa.ClotheColor.Blue_Light = pa.ClotheColor.BLUE_01
pa.ClotheColor.Blue_Medium = pa.ClotheColor.BLUE_02
pa.ClotheColor.Blue_Dark = pa.ClotheColor.BLUE_03
pa.ClotheColor.Gray_Light = pa.ClotheColor.GRAY_01
pa.ClotheColor.Gray_Dark = pa.ClotheColor.GRAY_02
pa.ClotheColor.Heather = pa.ClotheColor.HEATHER
pa.ClotheColor.Pastel_Blue = pa.ClotheColor.PASTEL_BLUE
pa.ClotheColor.Pastel_Green = pa.ClotheColor.PASTEL_GREEN
pa.ClotheColor.Pastel_Orange = pa.ClotheColor.PASTEL_ORANGE
pa.ClotheColor.Pastel_Red = pa.ClotheColor.PASTEL_RED
pa.ClotheColor.Pastel_Yellow = pa.ClotheColor.PASTEL_YELLOW
pa.ClotheColor.Pink = pa.ClotheColor.PINK
pa.ClotheColor.Red = pa.ClotheColor.RED
pa.ClotheColor.White = pa.ClotheColor.WHITE
# Top/Hairstyle
pa.TopType.Bald_1 = pa.TopType.NO_HAIR
pa.TopType.Bald_2 = pa.TopType.SHORT_HAIR_SIDES
pa.TopType.Hat = pa.TopType.HAT
pa.TopType.Hijab = pa.TopType.HIJAB
pa.TopType.Turban = pa.TopType.TURBAN
pa.TopType.Winter_Hat_1 = pa.TopType.WINTER_HAT1
pa.TopType.Winter_Hat_2 = pa.TopType.WINTER_HAT2
pa.TopType.Winter_Hat_3 = pa.TopType.WINTER_HAT3
pa.TopType.Winter_Hat_4 = pa.TopType.WINTER_HAT4
pa.TopType.Long_Big = pa.TopType.LONG_HAIR_BIG_HAIR
pa.TopType.Long_Bob = pa.TopType.LONG_HAIR_BOB
pa.TopType.Long_Curly = pa.TopType.LONG_HAIR_CURLY
pa.TopType.Long_Curvy = pa.TopType.LONG_HAIR_CURVY
pa.TopType.Long_Dreads = pa.TopType.LONG_HAIR_DREADS
pa.TopType.Long_Fro = pa.TopType.LONG_HAIR_FRO
pa.TopType.Long_Fro_Band = pa.TopType.LONG_HAIR_FRO_BAND
pa.TopType.Long_Straight = pa.TopType.LONG_HAIR_STRAIGHT
pa.TopType.Long_Straight_Wavy = pa.TopType.LONG_HAIR_STRAIGHT2
pa.TopType.Long_Straight_Strand = pa.TopType.LONG_HAIR_STRAIGHT_STRAND
pa.TopType.Medium = pa.TopType.LONG_HAIR_NOT_TOO_LONG
pa.TopType.Medium_Dreads = pa.TopType.SHORT_HAIR_DREADS_02
pa.TopType.Bun = pa.TopType.LONG_HAIR_BUN
pa.TopType.Mia_Wallace = pa.TopType.LONG_HAIR_MIA_WALLACE
pa.TopType.Short_Dreads = pa.TopType.SHORT_HAIR_DREADS_01
pa.TopType.Short_Frizzle = pa.TopType.SHORT_HAIR_FRIZZLE
pa.TopType.Short_Mullet = pa.TopType.SHORT_HAIR_SHAGGY_MULLET
pa.TopType.Short_Curly = pa.TopType.SHORT_HAIR_SHORT_CURLY
pa.TopType.Short_Flat = pa.TopType.SHORT_HAIR_SHORT_FLAT
pa.TopType.Short_Round = pa.TopType.SHORT_HAIR_SHORT_ROUND
pa.TopType.Short_Waved = pa.TopType.SHORT_HAIR_SHORT_WAVED
pa.TopType.Short_Caesar_1 = pa.TopType.SHORT_HAIR_THE_CAESAR
pa.TopType.Short_Caesar_2 = pa.TopType.SHORT_HAIR_THE_CAESAR_SIDE_PART
# Mouth
pa.MouthType.Happy = pa.FacialHairType.DEFAULT
pa.MouthType.Concerned = pa.MouthType.CONCERNED
pa.MouthType.Disbelief = pa.MouthType.DISBELIEF
pa.MouthType.Eating = pa.MouthType.EATING
pa.MouthType.Grimace = pa.MouthType.GRIMACE
pa.MouthType.Sad = pa.MouthType.SAD
pa.MouthType.Shocked = pa.MouthType.SCREAM_OPEN
pa.MouthType.Serious = pa.MouthType.SERIOUS
pa.MouthType.Smile = pa.MouthType.SMILE
pa.MouthType.Tongue = pa.MouthType.TONGUE
pa.MouthType.Twinkle = pa.MouthType.TWINKLE
pa.MouthType.Vomit = pa.MouthType.VOMIT
# Eye
pa.EyesType.Open = pa.EyesType.DEFAULT
pa.EyesType.Close = pa.EyesType.CLOSE
pa.EyesType.Cry = pa.EyesType.CRY
pa.EyesType.Dizzy = pa.EyesType.DIZZY
pa.EyesType.Eye_Roll = pa.EyesType.EYE_ROLL
pa.EyesType.Happy = pa.EyesType.HAPPY
pa.EyesType.Hearts = pa.EyesType.HEARTS
pa.EyesType.Side = pa.EyesType.SIDE
pa.EyesType.Squint = pa.EyesType.SQUINT
pa.EyesType.Surprised = pa.EyesType.SURPRISED
pa.EyesType.Wink_1 = pa.EyesType.WINK
pa.EyesType.Wink_2 = pa.EyesType.WINK_WACKY
# Eyebrows
pa.EyebrowType.Happy_1 = pa.EyebrowType.DEFAULT
pa.EyebrowType.Happy_2 = pa.EyebrowType.DEFAULT_NATURAL
pa.EyebrowType.Angry_1 = pa.EyebrowType.ANGRY
pa.EyebrowType.Angry_2 = pa.EyebrowType.ANGRY_NATURAL
pa.EyebrowType.Flat = pa.EyebrowType.FLAT_NATURAL
pa.EyebrowType.Excited_1 = pa.EyebrowType.RAISED_EXCITED
pa.EyebrowType.Excited_2 = pa.EyebrowType.RAISED_EXCITED_NATURAL
pa.EyebrowType.Sad_1 = pa.EyebrowType.SAD_CONCERNED
pa.EyebrowType.Sad_2 = pa.EyebrowType.SAD_CONCERNED_NATURAL
pa.EyebrowType.Sad_3 = pa.EyebrowType.FROWN_NATURAL
pa.EyebrowType.Unibrow = pa.EyebrowType.UNI_BROW_NATURAL
pa.EyebrowType.Confused_1 = pa.EyebrowType.UP_DOWN
pa.EyebrowType.Confused_2 = pa.EyebrowType.UP_DOWN_NATURAL
# Glasses
pa.AccessoriesType.Default = pa.AccessoriesType.DEFAULT
pa.AccessoriesType.Kurt = pa.AccessoriesType.KURT
pa.AccessoriesType.Square_White = pa.AccessoriesType.PRESCRIPTION_01
pa.AccessoriesType.Square_Black = pa.AccessoriesType.PRESCRIPTION_02
pa.AccessoriesType.Round = pa.AccessoriesType.ROUND
pa.AccessoriesType.Sunglasses = pa.AccessoriesType.SUNGLASSES
pa.AccessoriesType.Wayfarers = pa.AccessoriesType.WAYFARERS
# Clothe
pa.ClotheType.Collar_Sweater = pa.ClotheType.COLLAR_SWEATER
pa.ClotheType.Graphic_Shirt = pa.ClotheType.GRAPHIC_SHIRT
pa.ClotheType.Hoodie = pa.ClotheType.HOODIE
pa.ClotheType.Shirt_Crew = pa.ClotheType.SHIRT_CREW_NECK
pa.ClotheType.Shirt_Scoop = pa.ClotheType.SHIRT_SCOOP_NECK
pa.ClotheType.Shirt_V_Neck = pa.ClotheType.SHIRT_V_NECK
# Clothe Graphic
pa.ClotheGraphicType.Bat = pa.ClotheGraphicType.BAT
pa.ClotheGraphicType.Deer = pa.ClotheGraphicType.DEER
pa.ClotheGraphicType.Diamond = pa.ClotheGraphicType.DIAMOND
pa.ClotheGraphicType.Hola = pa.ClotheGraphicType.HOLA
pa.ClotheGraphicType.Pizza = pa.ClotheGraphicType.PIZZA
pa.ClotheGraphicType.Bear = pa.ClotheGraphicType.BEAR
pa.ClotheGraphicType.Skull_1 = pa.ClotheGraphicType.SKULL
pa.ClotheGraphicType.Skull_2 = pa.ClotheGraphicType.SKULL_OUTLINE

def page_gender(state):
    list_gender_option = ['Male','Female','Other']
    state.gender_option = st.selectbox("Please select your gender",list_gender_option, list_gender_option.index(state.gender_option) if state.gender_option else 0)
    if state.gender_option == 'Male': 
        state.list_background = ['Circle','Transparent']
        state.list_skin_color = ['Pale','Tanned','Yellow','Black','Light','Brown','Dark_Brown']
        state.list_top_type =  ['Short_Flat','Short_Curly','Short_Round','Short_Waved','Short_Dreads','Short_Frizzle','Short_Mullet','Short_Caesar_1','Short_Caesar_2','Long_Fro','Medium_Dreads',
                                'Bald_1','Bald_2','Long_Straight_Wavy','Hat','Turban','Winter_Hat_1','Winter_Hat_2','Winter_Hat_3',]
                                #Removed 'EYE_PATCH' ''LONG_HAIR_SHAVED_SIDES' 'LONG_HAIR_FRIDA'
        state.list_hair_color = ['Blonde','Blonde_Golden','Brown','Brown_Dark','Black','Auburn','Silver_Gray']
        state.list_hat_color = ['Black','Blue_Dark','Gray_Light','Gray_Dark','Heather','White']
        state.list_eyebrow_type = ['Happy_1','Happy_2','Angry_1','Angry_2','Excited_1','Excited_2','Unibrow']
        state.list_eye_type = ['Open','Close','Dizzy','Eye_Roll','Happy','Side','Squint','Surprised','Wink_1','Wink_2']
        state.list_glasses_type = ['Default','Square_White','Square_Black','Round','Sunglasses','Wayfarers']
        state.list_mouth_type = ['Smile','Happy','Serious','Grimace','Shocked','Disbelief','Vomit']
        state.list_facial_hair_type = ['Default','Light','Medium','Majestic','Moustache_Fancy','Moustache_Magnum']
        state.list_facial_hair_color = ['Pastel_Yellow','White','Gray_Light','Gray_Dark','Heather','Black']
        state.list_clothe_type = ['Hoodie','Collar_Sweater','Shirt_Crew','Shirt_V_Neck','Graphic_Shirt']
                                    #Rmoved 'BLAZER_SHIRT' 'BLAZER_SWEATER' 'Overall'
        state.list_clothe_color = ['Black','Blue_Light','Blue_Medium','Blue_Dark','Gray_Light','Gray_Dark','Heather','Pastel_Blue','Pastel_Green','Pastel_Orange','Red','White']
        state.list_clothe_graphic_type = ['Bat','Deer','Diamond','Hola','Pizza','Bear','Skull_1','Skull_2']
        # Default Male Avatar
        state.initial_background = 'Circle'
        state.initial_skin_color = 'Pale'
        state.initial_top_type = 'Short_Flat'
        state.initial_hair_color = 'Blonde'
        state.initial_hat_color = 'BLACK'
        state.initial_eyebrow_type = 'Happy_1'
        state.initial_eye_type = 'Open'
        state.initial_glasses_type = 'Default'
        state.initial_mouth_type = 'Smile'
        state.initial_facial_hair_type = 'Default'
        state.initial_facial_hair_color = 'Pastel_Yellow'
        state.initial_clothe_type ='Hoodie'
        state.initial_clothe_color = 'BLACK'
        state.initial_clothe_graphic_type ='Bat'

    if state.gender_option == 'Female':
        state.list_background = ['Circle','Transparent']
        state.list_skin_color = ['Pale','Tanned','Yellow','Black','Light','Brown','Dark_Brown']
        state.list_top_type = ['Long_Straight','Long_Straight_Wavy','Long_Straight_Strand','Long_Curvy','Long_Big','Long_Bob','Long_Curly','Long_Dreads','Long_Fro','Long_Fro_Band','Medium',
                                'Mia_Wallace','Bun','Short_Flat','Hijab','Winter_Hat_1','Winter_Hat_2','Winter_Hat_3','Winter_Hat_4']
                                    #Removed 'EYE_PATCH' ''LONG_HAIR_SHAVED_SIDES' 'LONG_HAIR_FRIDA'
        state.list_hair_color = ['Blonde','Blonde_Golden','Brown','Brown_Dark','Black','Auburn','Pastel_Pink','Platinum','Red','Silver_Gray']
        state.list_hat_color = ['Pink','Blue_Light','Blue_Medium','Pastel_Blue','Pastel_Green','Pastel_Orange','Pastel_Red','Pastel_Yellow','Red','White','Black','Blue_Dark','Gray_Light','Gray_Dark','Heather']
        state.list_eyebrow_type = ['Happy_1','Happy_2','Flat','Excited_1','Excited_2','Sad_1','Sad_2','Sad_3','Confused_1','Confused_2']
        state.list_eye_type = ['Open','Close','Hearts','Cry','Dizzy','Eye_Roll','Happy','Side','Squint','Surprised','Wink_1','Wink_2']
        state.list_glasses_type = ['Default','Kurt','Square_White','Square_Black','Round','Sunglasses','Wayfarers']
        state.list_mouth_type = ['Smile','Happy','Twinkle','Eating','Tongue','Serious','Sad','Disbelief','Concerned']
        state.list_facial_hair_type = []
        state.list_facial_hair_color = []
        state.list_clothe_type = ['Shirt_Scoop','Shirt_V_Neck','Shirt_Crew','Collar_Sweater','Hoodie','Graphic_Shirt']
                                    #Rmoved 'BLAZER_SHIRT' 'BLAZER_SWEATER' 'Overall'
        state.list_clothe_color = ['Pink','Red','Pastel_Red','Pastel_Orange','Pastel_Green','Pastel_Blue','Pastel_Yellow','Blue_Light','Blue_Medium','Blue_Dark','Gray_Light','Gray_Dark','Heather','Black','White']
        state.list_clothe_graphic_type = ['Bat','Deer','Diamond','Hola','Pizza','Bear','Skull_1','Skull_2']
        # Default Female Avatar
        state.initial_background = 'Circle'
        state.initial_skin_color = 'Pale'
        state.initial_top_type = 'Long_Straight'
        state.initial_hair_color = 'Blonde'
        state.initial_hat_color = 'Pink'
        state.initial_eyebrow_type = 'Happy_1'
        state.initial_eye_type = 'Open'
        state.initial_glasses_type = 'Default'
        state.initial_mouth_type = 'Smile'
        state.initial_facial_hair_type = 'Default'
        state.initial_facial_hair_color = 'Black'
        state.initial_clothe_type ='Shirt_Scoop'
        state.initial_clothe_color = 'Pink'
        state.initial_clothe_graphic_type ='Bat'

    if state.gender_option == 'Other':
        state.list_background = ['Circle','Transparent']
        state.list_skin_color = ['Pale','Tanned','Yellow','Black','Light','Brown','Dark_Brown']
        state.list_top_type = ['Bald_1','Bald_2','Hat','Hijab','Turban','Winter_Hat_1','Winter_Hat_2','Winter_Hat_3','Winter_Hat_4','Long_Big','Long_Bob','Long_Curly','Long_Curvy','Long_Dreads','Long_Fro','Long_Fro_Band','Long_Straight',
                                'Long_Straight_Wavy','Long_Straight_Strand','Medium','Medium_Dreads','Bun','Mia_Wallace','Short_Dreads','Short_Frizzle','Short_Mullet','Short_Curly','Short_Flat','Short_Round','Short_Waved',
                                'Short_Caesar_1','Short_Caesar_2']
                                    #Removed 'EYE_PATCH' ''LONG_HAIR_SHAVED_SIDES' 'LONG_HAIR_FRIDA'
        state.list_hair_color = ['Blonde','Auburn','Black','Blonde_Golden','Brown','Brown_Dark','Pastel_Pink','Platinum','Red','Silver_Gray']
        state.list_hat_color = ['Black','Blue_Light','Blue_Medium','Blue_Dark','Gray_Light','Gray_Dark','Heather','Pastel_Blue','Pastel_Green','Pastel_Orange','Pastel_Red','Pastel_Yellow','Pink','Red','White']
        state.list_eyebrow_type = ['Happy_1','Happy_2','Angry_1','Angry_2','Flat','Excited_1','Excited_2','Sad_1','Sad_2','Sad_3','Unibrow','Confused_1','Confused_2']
        state.list_eye_type = ['Open','Close','Cry','Dizzy','Eye_Roll','Happy','Hearts','Side','Squint','Surprised','Wink_1','Wink_2']
        state.list_glasses_type = ['Default','Kurt','Square_White','Square_Black','Round','Sunglasses','Wayfarers']
        state.list_mouth_type = ['Smile','Happy','Concerned','Disbelief','Eating','Grimace','Sad','Shocked','Serious','Tongue','Twinkle','Vomit']
        state.list_facial_hair_type = ['Default','Light','Medium','Majestic','Moustache_Fancy','Moustache_Magnum']
        state.list_facial_hair_color = ['Pastel_Yellow','Gray_Light','Gray_Dark','Black','Blue_Light','Blue_Medium','Blue_Dark','Heather','Pastel_Blue','Pastel_Green','Pastel_Orange','Pastel_Red','Pink','Red','White']
        state.list_clothe_type = ['Shirt_Crew','Shirt_Scoop','Shirt_V_Neck','Hoodie','Collar_Sweater','Graphic_Shirt']
                                    #Rmoved 'BLAZER_SHIRT' 'BLAZER_SWEATER' 'Overall'
        state.list_clothe_color = ['Black','Blue_Light','Blue_Medium','Blue_Dark','Gray_Light','Gray_Dark','Heather','Pastel_Blue','Pastel_Green','Pastel_Orange','Pastel_Red','Pastel_Yellow','Pink','Red','White']
        state.list_clothe_graphic_type = ['Bat','Deer','Diamond','Hola','Pizza','Bear','Skull_1','Skull_2']
        # Default Other Avatar
        state.initial_background = 'Circle'
        state.initial_skin_color = 'Pale'
        state.initial_top_type = 'Bald_1'
        state.initial_hair_color = 'Blonde'
        state.initial_hat_color = 'Black'
        state.initial_eyebrow_type = 'Happy_1'
        state.initial_eye_type = 'Open'
        state.initial_glasses_type = 'Default'
        state.initial_mouth_type = 'Smile'
        state.initial_facial_hair_type = 'Default'
        state.initial_facial_hair_color = 'Pastel_Yellow'
        state.initial_clothe_type ='Shirt_Crew'
        state.initial_clothe_color = 'Black'
        state.initial_clothe_graphic_type ='Bat'

    display_state_values(state)


def page_background(state):
    state.option_background = st.selectbox('Background',state.list_background, state.list_background.index(state.option_background) if state.option_background else 0)
    display_state_values(state)
    
def page_skin_color(state):
    state.option_skin_color = st.selectbox('Skin Color',state.list_skin_color, state.list_skin_color.index(state.option_skin_color) if state.option_skin_color else 0)
    display_state_values(state)

def page_top_type(state):
    state.option_top_type = st.selectbox('Hairstyle/Hat',state.list_top_type, state.list_top_type.index(state.option_top_type) if state.option_top_type else 0)
    display_state_values(state)

def page_hair_color(state):
    state.option_hair_color = st.selectbox('Hair Color (applicable if a hairstyle is selected)',state.list_hair_color, state.list_hair_color.index(state.option_hair_color) if state.option_hair_color else 0)
    display_state_values(state)

def page_hat_color(state):
    state.option_hat_color = st.selectbox('Hat Color (applicable if a hat is selected)',state.list_hat_color, state.list_hat_color.index(state.option_hat_color) if state.option_hat_color else 0)
    display_state_values(state)
    
def page_eyebrow_type(state):
    state.option_eyebrow_type = st.selectbox('Eyebrow Type',state.list_eyebrow_type, state.list_eyebrow_type.index(state.option_eyebrow_type) if state.option_eyebrow_type else 0)
    display_state_values(state)

def page_eye_type(state):
    state.option_eye_type = st.selectbox('Eye Type',state.list_eye_type, state.list_eye_type.index(state.option_eye_type) if state.option_eye_type else 0)
    display_state_values(state)

def page_glasses_type(state):
    state.option_glasses_type = st.selectbox('Glasses',state.list_glasses_type, state.list_glasses_type.index(state.option_glasses_type) if state.option_glasses_type else 0)
    display_state_values(state)

def page_mouth_type(state):
    state.option_mouth_type = st.selectbox('Mouth',state.list_mouth_type, state.list_mouth_type.index(state.option_mouth_type) if state.option_mouth_type else 0)
    display_state_values(state)

def page_facial_hair_type(state):
    state.option_facial_hair_type = st.selectbox('Facial Hair Type',state.list_facial_hair_type, state.list_facial_hair_type.index(state.option_facial_hair_type) if state.option_facial_hair_type else 0)
    display_state_values(state)

def page_facial_hair_color(state):
    state.option_facial_hair_color = st.selectbox('Facial Hair Color (applicable if a facial hair is selected)',state.list_facial_hair_color, state.list_facial_hair_color.index(state.option_facial_hair_color) if state.option_facial_hair_color else 0)
    display_state_values(state)

def page_clothe_type(state):
    state.option_clothe_type = st.selectbox('Clothing',state.list_clothe_type, state.list_clothe_type.index(state.option_clothe_type) if state.option_clothe_type else 0)
    display_state_values(state)

def page_clothe_color(state):
    state.option_clothe_color = st.selectbox('Clothing Color',state.list_clothe_color, state.list_clothe_color.index(state.option_clothe_color) if state.option_clothe_color else 0)
    display_state_values(state)

def page_clothe_graphic(state):
    state.option_clothe_graphic_type = st.selectbox('Clothing Graphic (applicable if GRAPHIC_SHIRT is selected)',state.list_clothe_graphic_type, state.list_clothe_graphic_type.index(state.option_clothe_graphic_type) if state.option_clothe_graphic_type else 0)
    display_state_values(state)

# Link can be changed to survey
def page_redirect(state):
    link = '[Click here to go back to survey](http://github.com)'
    st.markdown(link, unsafe_allow_html=True)
   # st.button('Click to go back to survey')
    display_state_values(state)

                


# Static Part
def display_state_values(state):
    avatar = pa.PyAvataaar(
        style=getattr(pa.AvatarStyle, str(state.option_background), getattr(pa.AvatarStyle, str(state.initial_background))),
        skin_color=getattr(pa.SkinColor, str(state.option_skin_color), getattr(pa.SkinColor, str(state.initial_skin_color))),
        hair_color=getattr(pa.HairColor, str(state.option_hair_color), getattr(pa.HairColor, str(state.initial_hair_color))),
        facial_hair_type=getattr(pa.FacialHairType, str(state.option_facial_hair_type), getattr(pa.FacialHairType, str(state.initial_facial_hair_type))),
        facial_hair_color=getattr(pa.ClotheColor, str(state.option_facial_hair_color), getattr(pa.ClotheColor, str(state.initial_facial_hair_color))),
        top_type=getattr(pa.TopType, str(state.option_top_type), getattr(pa.TopType, str(state.initial_top_type))),
        hat_color=getattr(pa.ClotheColor, str(state.option_hat_color), getattr(pa.ClotheColor, str(state.initial_hat_color))),
        mouth_type=getattr(pa.MouthType, str(state.option_mouth_type), getattr(pa.MouthType, str(state.initial_mouth_type))),
        eye_type=getattr(pa.EyesType, str(state.option_eye_type), getattr(pa.EyesType, str(state.initial_eye_type))),
        eyebrow_type=getattr(pa.EyebrowType, str(state.option_eyebrow_type), getattr(pa.EyebrowType, str(state.initial_eyebrow_type))),
        nose_type=pa.NoseType.DEFAULT,
        accessories_type=getattr(pa.AccessoriesType, str(state.option_glasses_type), getattr(pa.AccessoriesType, str(state.initial_glasses_type))),
        clothe_type=getattr(pa.ClotheType, str(state.option_clothe_type), getattr(pa.ClotheType, str(state.initial_clothe_type))),
        clothe_color=getattr(pa.ClotheColor, str(state.option_clothe_color), getattr(pa.ClotheColor, str(state.initial_clothe_color))),
        clothe_graphic_type=getattr(pa.ClotheGraphicType, str(state.option_clothe_graphic_type), getattr(pa.ClotheGraphicType, str(state.initial_clothe_graphic_type))),
)
    
    rendered_avatar = avatar.render_png_file('avatar.png')
    image = Image.open('avatar.png')
    st.image(image)
    st.markdown(imagedownload('avatar.png'), unsafe_allow_html=True)

# Custom function by dataprofessor for encoding an donwloading avatar image
def imagedownload(filename):
    image_file = open(filename, 'rb')
    b64 = base64.b64encode(image_file.read()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download {filename}</a>'
    return href 

# SessionState code from st_demo_settings.py

class _SessionState:
    
    def __init__(self, session, hash_funcs):
        """Initialize SessionState instance."""
        self.__dict__["_state"] = {
            "data": {},
            "hash": None,
            "hasher": _CodeHasher(hash_funcs),
            "is_rerun": False,
            "session": session,
        }

    def __call__(self, **kwargs):
        """Initialize state data once."""
        for item, value in kwargs.items():
            if item not in self._state["data"]:
                self._state["data"][item] = value

    def __getitem__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)
        
    def __getattr__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)

    def __setitem__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value

    def __setattr__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value
    
    def clear(self):
        """Clear session state and request a rerun."""
        self._state["data"].clear()
        self._state["session"].request_rerun()
    
    def sync(self):
        """Rerun the app with all state values up to date from the beginning to fix rollbacks."""

        # Ensure to rerun only once to avoid infinite loops
        # caused by a constantly changing state value at each run.
        #
        # Example: state.value += 1
        if self._state["is_rerun"]:
            self._state["is_rerun"] = False
        
        elif self._state["hash"] is not None:
            if self._state["hash"] != self._state["hasher"].to_bytes(self._state["data"], None):
                self._state["is_rerun"] = True
                self._state["session"].request_rerun()

        self._state["hash"] = self._state["hasher"].to_bytes(self._state["data"], None)


def _get_session():
    session_id = get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)

    if session_info is None:
        raise RuntimeError("Couldn't get your Streamlit Session object.")
    
    return session_info.session


def _get_state(hash_funcs=None):
    session = _get_session()

    if not hasattr(session, "_custom_session_state"):
        session._custom_session_state = _SessionState(session, hash_funcs)

    return session._custom_session_state


if __name__ == "__main__":
    main()
