
import streamlit as st
import clips
import logging

logging.basicConfig(level=15,format='%(message)s')

env = clips.Environment()
router = clips.LoggingRouter()
env.add_router(router)

#input
name = st.text_input("Enter your name")

#knowledge base
env.build('(deftemplate result (slot name))')
env.assert_string(f'(result(name"{name}"))')
#interface
env.run()

#output
results = []
for fact in env.facts():
    if fact.template.name == 'result':
        #output
        results = []
        for fact in env.facts():
            if fact.template.name =='result':
                results.append(fact['name']) #Why assert the fact?

        st.write(results[0],"output")