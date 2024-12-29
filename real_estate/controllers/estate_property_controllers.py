from odoo import http
from odoo.http import content_disposition, request
import io
import xlsxwriter

class EstatePropertyReportExcel(http.Controller):
    @http.route(['/download/estate-property-report-excel/<model("estate.property"):data>'],type='http', auth="user")
    def get_estate_property_report_excel(self, data=None, **args):
        response = request.make_response(
            None,
            headers=[
                ('Content-type', 'application/vnd.ms-excel'),
                ('Content-Disposition', content_disposition('Estate Property Report' + '.xlsx'))
            ]
        )

        # buat object workbook from library xlsxwriter
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in-memory': True})

        title_style = workbook.add_format({ "bold": True })
        uom_format = workbook.add_format({ 'num_format': '$#,##0' })

        # format untuk header
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': True,
            'valign': 'top',
            'align': 'center',
            'fg_color': '#1465B5',
            'font_color': 'white',
        })
        cell_format = workbook.add_format({
            'text_wrap': True,
            'valign': 'top',
            'border': 1
        })
        number_format = workbook.add_format({ 
            'align': 'center',
            'valign': 'top', 
            'border': 1 
        })

        for property in data:
            # untuk penamaan page sheets
            sheet = workbook.add_worksheet(property.name)

            sheet.write('A2', 'Report Estate Property', title_style)
            sheet.write('A3', 'Name: ')
            sheet.write('A4', 'Type: ')
            sheet.write('A5', 'Post Code: ')
            sheet.write('A6', 'Expected Price: ')
            sheet.write('A7', 'Property Offers: ')
            sheet.write('H3', 'Salesman: ')
            sheet.write('H4', 'Status: ')

            sheet.write('E3', property.name)
            sheet.write('E4', property.property_type_id.name)
            sheet.write('E5', property.postcode)
            sheet.write('E6', property.expected_price, uom_format)
            sheet.write('K3', property.salesman.name)
            sheet.write('K4', property.state)

            row = 8
            number = 1

            sheet.write(7, 0,  'No', header_format)
            sheet.write(7, 1,  'Price', header_format)
            sheet.write(7, 2,  'Partner', header_format)
            sheet.write(7, 3,  'Validity (days)', header_format)
            sheet.write(7, 4,  'Deadline', header_format)
            sheet.write(7, 5,  'State', header_format)

            # property.estate.offer
            estate_property_offers = request.env['estate.property.offer'].search([('property_id', '=', property.id)])
            for offer in estate_property_offers:
                sheet.write(row, 0, number, number_format)
                sheet.write(row, 1, offer.price, cell_format)
                sheet.write(row, 2, offer.partner_id.name, cell_format)
                sheet.write(row, 3, offer.validity, cell_format)
                sheet.write(row, 4, offer.date_deadline, cell_format)
                sheet.write(row, 5, offer.status, cell_format)

                row += 1
                number += 1

        # memasukkan file excel yang sudah di generate ke response dan return
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
        return response