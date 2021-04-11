from fpdf import FPDF

def createpdf(students,mom,flu):
    pdf=FPDF()
    i=2
    key=0
    if(len(students)>0):
        pdf.add_page()
        pdf.set_font("Arial",'B', size=17)
        pdf.cell(200,10,txt='Attendance List: ',ln=1)
        pdf.set_font("Arial", size=15)
        for x1 in students:
            pdf.cell(200,10,txt=x1,ln=i)
            i=i+1
        key=1
    if(len(mom)>0):
        i=2
        pdf.add_page()
        pdf.set_font("Arial",'B', size=17)
        pdf.cell(200,10,txt='MOM: ',ln=1)
        pdf.set_font("Arial", size=15)
        for x1 in mom:
            pdf.cell(200,10,txt=x1,ln=i)
            i=i+1
        key=1
    if(len(flu)>0):
        i=2
        flu1=set(flu)
        flu2=list(flu1)
        pdf.add_page()
        pdf.set_font("Arial",'B', size=17)
        pdf.cell(200,10,txt='Profanity: ',ln=1)
        pdf.set_font("Arial", size=15)
        for x1 in flu2:
            pdf.cell(200,10,txt=x1,ln=i)
            i=i+1
        key=1
        if(key==1):
             pdf.output("name.pdf")