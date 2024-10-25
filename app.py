import streamlit as st
import streamlit.components.v1 as components
from functions import *
import pandas as pd
from io import BytesIO

st.set_page_config(
     page_title = 'LENS: LEARNING ENTITIES FROM NARRATIVES OF SKIN CANCER',
     page_icon = '🎗', #🔍🔎🎗
     layout = "wide",
     initial_sidebar_state = "expanded",
     menu_items={
         'Get Help': "https://github.com/4dpicture/LENS",
         'Report a bug': "https://github.com/4dpicture/LENS",
        #  'About': '''## Understanding imprecise space and time in narratives through qualitative representations, reasoning, and visualisation'''
     }
 )


st.sidebar.image('lens_logo_v1.png')
st.markdown('#### ⚙️ Extracting LENS Entities')
# st.sidebar.markdown('### 🗺️ LENS Explorer')

EXAMPLE_TEXT = ''
SCT_TEXT = ''
MCT_TEXT = ''

option_text = st.sidebar.radio('How do you want to input your text?', 
                                ['Use an example file', 'Paste copied text', 'Upload data file'])
option_mapping = st.sidebar.radio('Mappings', ['Lens','Snomed CT', 'MedCAT'])

if option_text == 'Paste copied text' and option_mapping == 'Lens':
    EXAMPLE_TEXT = st.text_area('Paste text to tag', height=300)
elif option_text == 'Paste copied text' and option_mapping == 'Snomed CT':
    SCT_TEXT = st.text_area('Paste text to tag', height=300)
    # st.info(f'''**'{option_mapping}'** feature is still under construction''', icon="🚧")
elif option_text == 'Paste copied text' and option_mapping == 'MedCAT':
    MCT_TEXT = st.text_area('Paste text to tag', height=300)
    # st.info(f'''**'{option_mapping}'** feature is still under construction''', icon="🚧")

elif option_text == 'Use an example file' and option_mapping == 'Lens':
    fpath = os.path.join(EXAMPLES_DIR, st.selectbox('Choose a file to work with', ['Select file...'] + example_files))
    EXAMPLE_TEXT = None if fpath.endswith('Select file...') else open(fpath, encoding='utf-8').read()  
    show_original_text = st.checkbox('Show original text')
    if show_original_text:
        # st.markdown(show_plain_text(EXAMPLE_TEXT), unsafe_allow_html=True)
        components.html(show_plain_text(EXAMPLE_TEXT), height=300, scrolling=True)
elif option_text == 'Use an example file' and option_mapping == 'Snomed CT':
    fpath = os.path.join(EXAMPLES_DIR, st.selectbox('Choose a file to work with', ['Select file...'] + example_files))
    SCT_TEXT = None if fpath.endswith('Select file...') else open(fpath, encoding='utf-8').read()  
    show_original_text = st.checkbox('Show original text')
    if show_original_text:
        # st.markdown(show_plain_text(EXAMPLE_TEXT), unsafe_allow_html=True)
        components.html(show_plain_text(SCT_TEXT), height=300, scrolling=True)
    # st.info(f'''**'{option_mapping}'** feature is still under construction''', icon="🚧")
elif option_text == 'Use an example file' and option_mapping == 'MedCAT':
    fpath = os.path.join(EXAMPLES_DIR, st.selectbox('Choose a file to work with', ['Select file...'] + example_files))
    MCT_TEXT = None if fpath.endswith('Select file...') else open(fpath, encoding='utf-8').read()  
    show_original_text = st.checkbox('Show original text')
    if show_original_text:
        # st.markdown(show_plain_text(EXAMPLE_TEXT), unsafe_allow_html=True)
        components.html(show_plain_text(MCT_TEXT), height=300, scrolling=True)

elif option_text == 'Upload data file' and option_mapping == 'Lens':
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        EXAMPLE_TEXT = str(uploaded_file.read())[2:-1] #.getvalue()
        agree = st.checkbox('Show original text')
        if agree:
            # st.markdown(show_plain_text(EXAMPLE_TEXT), unsafe_allow_html=True)
            components.html(show_plain_text(EXAMPLE_TEXT), height=300, scrolling=True)
elif option_text == 'Upload data file' and option_mapping == 'Snomed CT':
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        SCT_TEXT = str(uploaded_file.read())[2:-1] #.getvalue()
        agree = st.checkbox('Show original text')
        if agree:
            # st.markdown(show_plain_text(EXAMPLE_TEXT), unsafe_allow_html=True)
            components.html(show_plain_text(SCT_TEXT), height=300, scrolling=True)
elif option_text == 'Upload data file' and option_mapping == 'MedCAT':
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        MCT_TEXT = str(uploaded_file.read())[2:-1] #.getvalue()
        agree = st.checkbox('Show original text')
        if agree:
            # st.markdown(show_plain_text(EXAMPLE_TEXT), unsafe_allow_html=True)
            components.html(show_plain_text(MCT_TEXT), height=300, scrolling=True)

if EXAMPLE_TEXT and not SCT_TEXT and not MCT_TEXT:
    st.sidebar.markdown('---')
    st.sidebar.write('Select tags to visualize:')

    all_entities = {ent['start_index']:(len(ent['entity']), ent['entity'], ent['label']) for ent in lens.get_entities(EXAMPLE_TEXT)}

    def sel_callback():
        st.session_state.CANC_T = st.session_state.sel_all
        st.session_state.STG = st.session_state.sel_all
        st.session_state.SYM = st.session_state.sel_all
        st.session_state.TRT = st.session_state.sel_all
        st.session_state.POB = st.session_state.sel_all
        st.session_state.MED = st.session_state.sel_all
        st.session_state.ADV_EFF = st.session_state.sel_all
        st.session_state.EGY = st.session_state.sel_all
        st.session_state.INV = st.session_state.sel_all
        st.session_state.RES = st.session_state.sel_all
        st.session_state.DIAG = st.session_state.sel_all
        st.session_state.MHD = st.session_state.sel_all
        st.session_state.SIZE = st.session_state.sel_all
        st.session_state.NUM = st.session_state.sel_all
        st.session_state.DUR = st.session_state.sel_all
        st.session_state.AGE = st.session_state.sel_all
        st.session_state.GENDER = st.session_state.sel_all
        st.session_state.AG = st.session_state.sel_all
        st.session_state.EMO = st.session_state.sel_all
        st.session_state.MET = st.session_state.sel_all
        st.session_state.EXP = st.session_state.sel_all
        st.session_state.PPL = st.session_state.sel_all
        st.session_state.GPE = st.session_state.sel_all
        st.session_state.ORG = st.session_state.sel_all
        
    def get_ents(sel_tags):
        entities={}
        for opt, tag_class in sel_tags:
            if opt: entities = merge_entities(entities, 
                {i:(l, e, t) for i, (l, e, t) in all_entities.items() if t in tag_class})
        return entities
    
    opt_all = st.sidebar.checkbox('All tags', key='sel_all', on_change=sel_callback)
    opt_canc = st.sidebar.checkbox('Cancer Type: CANC_T', key='CANC_T')
    opt_stg = st.sidebar.checkbox('Staging and grading: STG', key='STG')
    opt_sym = st.sidebar.checkbox('Symptom: SYM', key='SYM')
    opt_trt = st.sidebar.checkbox('Treatment: TRT', key='TRT')
    opt_inv = st.sidebar.checkbox('Investigation: INV', key='INV')
    opt_pob = st.sidebar.checkbox('Part of body: POB', key='POB')
    opt_age = st.sidebar.checkbox('Age: AGE', key = 'AGE')
    opt_gen = st.sidebar.checkbox('Gender: GENDER', key='GENDER')    
    opt_ag = st.sidebar.checkbox('Age/Gender: A/G', key = 'AG')
    opt_gpe = st.sidebar.checkbox('Geopolitical Entity: GPE', key = 'GPE')
    opt_org = st.sidebar.checkbox('Organization: ORG', key = 'ORG')
    opt_size = st.sidebar.checkbox('Size and shape of tumor: SIZE', key='SIZE')
    opt_num = st.sidebar.checkbox('Number: NUM', key='NUM')
    opt_dur = st.sidebar.checkbox('Duration: DUR', key='DUR')
    opt_egy = st.sidebar.checkbox('Etiology: EGY', key='EGY')
    opt_res = st.sidebar.checkbox('Result: RES', key='RES')
    opt_emo = st.sidebar.checkbox('Emotion: EMO', key='EMO')
    opt_met = st.sidebar.checkbox('Metaphor: MET', key = 'MET')
    opt_exp = st.sidebar.checkbox('Expressions: EXP', key='EXP')    
    opt_ppl = st.sidebar.checkbox('People (Cancer Care Team): PPL', key = 'PPL')
    opt_mhd = st.sidebar.checkbox('Mental Health Diagnosis: MHD', key = 'MHD')
    opt_diag = st.sidebar.checkbox('Diagnosis of other disease: DIAG', key = 'DIAG')
    opt_adv = st.sidebar.checkbox('Adverse Effects: ADV_EFF', key='ADV_EFF')
    opt_med = st.sidebar.checkbox('Medication: MED', key='MED')

    select_tags = [(opt_canc, 'CANC_T'), (opt_stg, 'STG'), (opt_sym, 'SYM'), (opt_trt, 'TRT'), (opt_inv, 'INV'), (opt_pob, 'POB'), (opt_age, 'AGE'), (opt_diag, 'DIAG'),
                   (opt_gen, 'GENDER'), (opt_ag, 'AG'), (opt_gpe, 'GPE'), (opt_org, 'ORG'), (opt_size, 'SIZE'), (opt_num, 'NUM'), (opt_dur, 'DUR'), (opt_adv, 'ADV_EFF'),
                   (opt_egy, 'EGY'), (opt_res, 'RES'), (opt_emo, 'EMO'), (opt_met, 'MET'), (opt_exp, 'EXP'), (opt_ppl, 'PPL'), (opt_mhd, 'MHD'), (opt_med, 'MED')
                ]
    if opt_all:
        # st.markdown('##### ⚙️ LENS Entities')

        # st.markdown(extractor.visualize(all_entities), unsafe_allow_html=True)
        st.markdown(visualize(EXAMPLE_TEXT, get_ents(select_tags)), unsafe_allow_html=True)        

        # components.html(extractor.visualize(all_entities), height=400, scrolling=True) 
        
        # st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown('##### ⚙️ Tabular Format')

        entities_lens = lens.get_entities(EXAMPLE_TEXT)
        # Convert entities to a DataFrame for display
        entities_df = pd.DataFrame(entities_lens)
        st.dataframe(entities_df)  # Display as a DataFrame

        # Function to convert DataFrame to Excel in memory
        def convert_df_to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Entities')
            output.seek(0)  # Move the cursor to the beginning of the BytesIO buffer
            return output.getvalue()
                # Function to convert DataFrame to CSV in memory
        def convert_df_to_csv(df):
            output = BytesIO()
            df.to_csv(output, index=False)
            output.seek(0)  # Move cursor to the beginning
            return output.getvalue()

        if not entities_df.empty:
            excel_file = convert_df_to_excel(entities_df)
            csv_file = convert_df_to_csv(entities_df)
    
            st.download_button(
                    label="Download as Excel",
                    data=excel_file,
                    file_name="lens_entities.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

            st.download_button(
                    label="Download as CSV",
                    data=csv_file,
                    file_name="lens_entities.csv",
                    mime="text/csv",
                    key="download_csv"  # Optional: add a key for uniqueness
                )
        else:
            st.error("No entities to download.")
    elif any((opt_canc, opt_stg, opt_sym, opt_trt, opt_inv, opt_pob, opt_age, opt_diag,
              opt_gen, opt_ag, opt_gpe, opt_org, opt_size, opt_num, opt_dur, opt_adv,
              opt_egy, opt_res, opt_emo, opt_met, opt_exp, opt_ppl, opt_mhd, opt_med)): 
        
        st.markdown('##### ⚙️ LENS Entities')
        st.markdown(visualize(EXAMPLE_TEXT, get_ents(select_tags)), unsafe_allow_html=True)

        st.markdown("<br><br><br>", unsafe_allow_html=True)
    
        st.markdown('##### ⚙️ Tabular Format')

        entities_lens = lens.get_entities(EXAMPLE_TEXT)
        # Convert entities to a DataFrame for display
        entities_df = pd.DataFrame(entities_lens)
        st.dataframe(entities_df)  # Display as a DataFrame

        # Function to convert DataFrame to Excel in memory
        def convert_df_to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Entities')
            output.seek(0)  # Move the cursor to the beginning of the BytesIO buffer
            return output.getvalue()

        # Function to convert DataFrame to CSV in memory
        def convert_df_to_csv(df):
            output = BytesIO()
            df.to_csv(output, index=False)
            output.seek(0)  # Move cursor to the beginning
            return output.getvalue()

        if not entities_df.empty:
            excel_file = convert_df_to_excel(entities_df)
            csv_file = convert_df_to_csv(entities_df)


            st.download_button(
                    label="Download as Excel",
                    data=excel_file,
                    file_name="lens_entities.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

            st.download_button(
                    label="Download as CSV",
                    data=csv_file,
                    file_name="lens_entities.csv",
                    mime="text/csv",
                    key="download_csv"  # Optional: add a key for uniqueness
                )
        else:
            st.error("No entities to download.")
    else:
        st.info(f'''**Select tag:** Select a tag class to visualize.''', icon="🧐")

# Assuming functions.lens2snomedct and functions.lens2medcat return a dictionary of entities
elif SCT_TEXT and not EXAMPLE_TEXT and not MCT_TEXT:
    entities_sct = lens.lens2snomedct(SCT_TEXT)
    # Convert entities to a DataFrame for display
    entities_df = pd.DataFrame(entities_sct)
    st.dataframe(entities_df)  # Display as a DataFrame

    # Function to convert DataFrame to Excel in memory
    def convert_df_to_excel(df):
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Entities')
        output.seek(0)  # Move the cursor to the beginning of the BytesIO buffer
        return output.getvalue()

    # Function to convert DataFrame to CSV in memory
    def convert_df_to_csv(df):
        output = BytesIO()
        df.to_csv(output, index=False)
        output.seek(0)  # Move cursor to the beginning
        return output.getvalue()

    if not entities_df.empty:
        excel_file = convert_df_to_excel(entities_df)
        csv_file = convert_df_to_csv(entities_df)

        st.download_button(
                label="Download as Excel",
                data=excel_file,
                file_name="lens2snomedct.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        st.download_button(
                label="Download as CSV",
                data=csv_file,
                file_name="lens2snomedct.csv",
                mime="text/csv",
                key="download_csv"  # Optional: add a key for uniqueness
            )
    else:
        st.error("No entities to download.")
elif MCT_TEXT and not EXAMPLE_TEXT and not SCT_TEXT:
    entities_mct = lens.lens2medcat(MCT_TEXT)
    # Convert entities to a DataFrame for display
    entities_df = pd.DataFrame(entities_mct)
    st.dataframe(entities_df)  # Display as a DataFrame

    # Function to convert DataFrame to Excel in memory
    def convert_df_to_excel(df):
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Entities')
        output.seek(0)  # Move the cursor to the beginning of the BytesIO buffer
        return output.getvalue()

    # Function to convert DataFrame to CSV in memory
    def convert_df_to_csv(df):
        output = BytesIO()
        df.to_csv(output, index=False)
        output.seek(0)  # Move cursor to the beginning
        return output.getvalue()

    if not entities_df.empty:
        excel_file = convert_df_to_excel(entities_df)
        csv_file = convert_df_to_csv(entities_df)

        st.download_button(
                label="Download as Excel",
                data=excel_file,
                file_name="lens2medcat.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        st.download_button(
                label="Download as CSV",
                data=csv_file,
                file_name="lens2medcat.csv",
                mime="text/csv",
                key="download_csv"  # Optional: add a key for uniqueness
            )
    else:
        st.error("No entities to download.")
else:
    st.error(f'''**NoInputText:** No input text to analyse...''', icon="🧐")
