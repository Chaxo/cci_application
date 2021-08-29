import streamlit as st
from streamlit.hashing import _CodeHasher
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server
import py_avataaars as pa
from PIL import Image
import base64
from random import randrange

def main():
    state = _get_state()
    pages = {
            "1. Background": page_background,
            "2. Skin Color": page_skin_color,
            "3. Head": page_top_type,
            "4. Hair Color": page_hair_color,
            "5. Hat Color": page_hat_color,
            "6. Eyebrow Type": page_eyebrow_type,
            "7. Eye Type": page_eye_type,
            "8. Glasses": page_glasses_type,
            "9. Mouth": page_mouth_type,
            "10. Facial Hair Type": page_facial_hair_type,
            "11. Facial Hair Color": page_facial_hair_color,
            "12. Clothe": page_clothe_type,
            "13. Clothe Color": page_clothe_color,
            "14. Clothe Graphic": page_clothe_graphic,
        }

    st.sidebar.title("Avatar Customization")
    page = st.sidebar.selectbox("Select out of 14 options", tuple(pages.keys()))

     # Display the selected page with the session state
    pages[page](state)

    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    state.sync()


st.header ('**Welcome to my avatar/character creation interface**')
st.markdown ("""
Preview of the avatar and download option (PNG file) can be found below. Customization options can be found on the left side.
""")


# Changing Avatar List Names
pa.FacialHairType.NONE = pa.FacialHairType.DEFAULT
pa.MouthType.HAPPY = pa.FacialHairType.DEFAULT
pa.EyesType.OPEN = pa.EyesType.DEFAULT
pa.AccessoriesType.NONE = pa.AccessoriesType.DEFAULT
pa.TopType.WINTER_HAT_USHANKA = pa.TopType.WINTER_HAT1
pa.TopType.WINTER_HAT_HOLIDAY = pa.TopType.WINTER_HAT2
pa.TopType.WINTER_HAT_BEANIE = pa.TopType.WINTER_HAT3
pa.TopType.WINTER_HAT_BEANIE_EARS = pa.TopType.WINTER_HAT4
pa.TopType.LONG_HAIR_STRAIGHT_WAVY = pa.TopType.LONG_HAIR_STRAIGHT2
pa.TopType.SHORT_HAIR_DREADS_SHORT = pa.TopType.SHORT_HAIR_DREADS_01
pa.TopType.SHORT_HAIR_DREADS_LONG = pa.TopType.SHORT_HAIR_DREADS_02
pa.ClotheColor.BLUE_LIGHT = pa.ClotheColor.BLUE_01
pa.ClotheColor.BLUE_MEDIUM = pa.ClotheColor.BLUE_02
pa.ClotheColor.BLUE_DARK = pa.ClotheColor.BLUE_03
pa.ClotheColor.GRAY_LIGHT = pa.ClotheColor.GRAY_01
pa.ClotheColor.GRAY_DARK = pa.ClotheColor.GRAY_02
pa.AccessoriesType.PRESCRIPTION_WHITE = pa.AccessoriesType.PRESCRIPTION_01
pa.AccessoriesType.PRESCRIPTION_BLACK = pa.AccessoriesType.PRESCRIPTION_02

def page_background(state):
    list_background = ['CIRCLE','TRANSPARENT']
    state.option_background = st.selectbox('Background',list_background, list_background.index(state.option_background) if state.option_background else 0)
    display_state_values(state)
    
def page_skin_color(state):
    list_skin_color = ['BLACK','TANNED','YELLOW','PALE','LIGHT','BROWN','DARK_BROWN']
    state.option_skin_color = st.selectbox('Skin Color',list_skin_color, list_skin_color.index(state.option_skin_color) if state.option_skin_color else 0)
    display_state_values(state)

def page_top_type(state):
    list_top_type = ['NO_HAIR','HAT','HIJAB','TURBAN','WINTER_HAT_USHANKA','WINTER_HAT_HOLIDAY','WINTER_HAT_BEANIE','WINTER_HAT_BEANIE_EARS','LONG_HAIR_BIG_HAIR','LONG_HAIR_BOB','LONG_HAIR_BUN',
                 'LONG_HAIR_CURLY','LONG_HAIR_CURVY','LONG_HAIR_DREADS','LONG_HAIR_FRO','LONG_HAIR_FRO_BAND','LONG_HAIR_NOT_TOO_LONG','LONG_HAIR_MIA_WALLACE',
                 'LONG_HAIR_STRAIGHT','LONG_HAIR_STRAIGHT_WAVY','LONG_HAIR_STRAIGHT_STRAND','SHORT_HAIR_DREADS_SHORT','SHORT_HAIR_DREADS_LONG','SHORT_HAIR_FRIZZLE',
                 'SHORT_HAIR_SHAGGY_MULLET','SHORT_HAIR_SHORT_CURLY','SHORT_HAIR_SHORT_FLAT','SHORT_HAIR_SHORT_ROUND','SHORT_HAIR_SHORT_WAVED','SHORT_HAIR_SIDES','SHORT_HAIR_THE_CAESAR','SHORT_HAIR_THE_CAESAR_SIDE_PART']
                  #Removed 'EYE_PATCH' ''LONG_HAIR_SHAVED_SIDES' 'LONG_HAIR_FRIDA'
    state.option_top_type = st.selectbox('Head',list_top_type, list_top_type.index(state.option_top_type) if state.option_top_type else 0)
    display_state_values(state)

def page_hair_color(state):
    list_hair_color = ['BLACK','AUBURN','BLONDE','BLONDE_GOLDEN','BROWN','BROWN_DARK','PASTEL_PINK','PLATINUM','RED','SILVER_GRAY']
    state.option_hair_color = st.selectbox('Hair Color (applicable if a hairstyle is selected)',list_hair_color, list_hair_color.index(state.option_hair_color) if state.option_hair_color else 0)
    display_state_values(state)

def page_hat_color(state):
    list_hat_color = ['BLACK','BLUE_LIGHT','BLUE_MEDIUM','BLUE_DARK','GRAY_LIGHT','GRAY_DARK','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']
    state.option_hat_color = st.selectbox('Hat Color (applicable if a hat is selected)',list_hat_color, list_hat_color.index(state.option_hat_color) if state.option_hat_color else 0)
    display_state_values(state)
    
def page_eyebrow_type(state):
    list_eyebrow_type = ['DEFAULT','DEFAULT_NATURAL','ANGRY','ANGRY_NATURAL','FLAT_NATURAL','RAISED_EXCITED','RAISED_EXCITED_NATURAL','SAD_CONCERNED','SAD_CONCERNED_NATURAL','UNI_BROW_NATURAL','UP_DOWN','UP_DOWN_NATURAL','FROWN_NATURAL']
    state.option_eyebrow_type = st.selectbox('Eyebrow Type',list_eyebrow_type, list_eyebrow_type.index(state.option_eyebrow_type) if state.option_eyebrow_type else 0)
    display_state_values(state)

def page_eye_type(state):
    list_eye_type = ['OPEN','CLOSE','CRY','DIZZY','EYE_ROLL','HAPPY','HEARTS','SIDE','SQUINT','SURPRISED','WINK','WINK_WACKY']
    state.option_eye_type = st.selectbox('Eye Type',list_eye_type, list_eye_type.index(state.option_eye_type) if state.option_eye_type else 0)
    display_state_values(state)

def page_glasses_type(state):
    list_glasses_type = ['NONE','KURT','PRESCRIPTION_WHITE','PRESCRIPTION_BLACK','ROUND','SUNGLASSES','WAYFARERS']
    state.option_glasses_type = st.selectbox('Glasses',list_glasses_type, list_glasses_type.index(state.option_glasses_type) if state.option_glasses_type else 0)
    display_state_values(state)

def page_mouth_type(state):
    list_mouth_type = ['HAPPY','CONCERNED','DISBELIEF','EATING','GRIMACE','SAD','SCREAM_OPEN','SERIOUS','SMILE','TONGUE','TWINKLE','VOMIT']
    state.option_mouth_type = st.selectbox('Mouth',list_mouth_type, list_mouth_type.index(state.option_mouth_type) if state.option_mouth_type else 0)
    display_state_values(state)

def page_facial_hair_type(state):
    list_facial_hair_type = ['NONE','BEARD_MEDIUM','BEARD_LIGHT','BEARD_MAJESTIC','MOUSTACHE_FANCY','MOUSTACHE_MAGNUM']
    state.option_facial_hair_type = st.selectbox('Facial Hair Type',list_facial_hair_type, list_facial_hair_type.index(state.option_facial_hair_type) if state.option_facial_hair_type else 0)
    display_state_values(state)

def page_facial_hair_color(state):
    list_facial_hair_color = ['BLACK','BLUE_LIGHT','BLUE_MEDIUM','BLUE_DARK','GRAY_LIGHT','GRAY_DARK','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']
    state.option_facial_hair_color = st.selectbox('Facial Hair Color',list_facial_hair_color, list_facial_hair_color.index(state.option_facial_hair_color) if state.option_facial_hair_color else 0)
    display_state_values(state)

def page_clothe_type(state):
    list_clothe_type = ['COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK']
                        #Rmoved 'BLAZER_SHIRT' 'BLAZER_SWEATER'
    state.option_clothe_type = st.selectbox('Clothe',list_clothe_type, list_clothe_type.index(state.option_clothe_type) if state.option_clothe_type else 0)
    display_state_values(state)

def page_clothe_color(state):
    list_clothe_color = ['BLACK','BLUE_LIGHT','BLUE_MEDIUM','BLUE_DARK','GRAY_LIGHT','GRAY_DARK','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']
    state.option_clothe_color = st.selectbox('Clothe Color',list_clothe_color, list_clothe_color.index(state.option_clothe_color) if state.option_clothe_color else 0)
    display_state_values(state)

def page_clothe_graphic(state):
    list_clothe_graphic_type = ['BAT','CUMBIA','DEER','DIAMOND','HOLA','PIZZA','RESIST','SELENA','BEAR','SKULL_OUTLINE','SKULL']
    state.option_clothe_graphic_type = st.selectbox('Clothe Graphic (applicable if GRAPHIC_SHIRT is selected)',list_clothe_graphic_type, list_clothe_graphic_type.index(state.option_clothe_graphic_type) if state.option_clothe_graphic_type else 0)
    display_state_values(state)


# Static Part
def display_state_values(state):
    avatar = pa.PyAvataaar(
        style=getattr(pa.AvatarStyle, str(state.option_background), pa.AvatarStyle.CIRCLE),
        skin_color=getattr(pa.SkinColor, str(state.option_skin_color), pa.SkinColor.BLACK),
        hair_color=getattr(pa.HairColor, str(state.option_hair_color), pa.HairColor.BLACK),
        facial_hair_type=getattr(pa.FacialHairType, str(state.option_facial_hair_type), pa.FacialHairType.DEFAULT),
        facial_hair_color=getattr(pa.ClotheColor, str(state.option_facial_hair_color), pa.HairColor.BLACK),
        top_type=getattr(pa.TopType, str(state.option_top_type), pa.TopType.NO_HAIR),
        hat_color=getattr(pa.ClotheColor, str(state.option_hat_color), pa.HairColor.BLACK),
        mouth_type=getattr(pa.MouthType, str(state.option_mouth_type), pa.MouthType.DEFAULT),
        eye_type=getattr(pa.EyesType, str(state.option_eye_type), pa.EyesType.DEFAULT),
        eyebrow_type=getattr(pa.EyebrowType, str(state.option_eyebrow_type), pa.EyebrowType.DEFAULT),
        nose_type=pa.NoseType.DEFAULT,
        accessories_type=getattr(pa.AccessoriesType, str(state.option_glasses_type), pa.AccessoriesType.DEFAULT),
        clothe_type=getattr(pa.ClotheType, str(state.option_clothe_type), pa.ClotheType.COLLAR_SWEATER),
        clothe_color=getattr(pa.ClotheColor, str(state.option_clothe_color), pa.HairColor.BLACK),
        clothe_graphic_type=getattr(pa.ClotheGraphicType, str(state.option_clothe_graphic_type), pa.ClotheGraphicType.BAT),
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
