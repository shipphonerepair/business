# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), request.controller == 'default' and request.function == 'index', URL('default', 'index')),
    (T('Screen Repair'), request.controller == 'default' and request.function == 'screen', URL('default', 'screen')),
    (T('Battery Replacement'), request.controller == 'default' and request.function == 'battery', URL('default', 'battery')),
    (T('Other Repair'), request.controller == 'default' and request.function == 'other', URL('default', 'other')),
    (T('Prices'), request.controller == 'default' and request.function == 'prices', URL('default', 'prices')),
    (T('Contact Me'), request.controller == 'default' and request.function == 'contact', URL('default', 'contact')),

]


def toggle_menuclass(cssclass='pressed', menuid='headermenu'):
    """This function changes the menu class to put pressed appearance"""

    positions = dict(
        index='',
        battery='-108px -115px',
        other='-211px -115px',
        contact='-315px -115px',
    )

    if request.function in positions.keys():
            jscript = """
            <script>
             $(document).ready(function(){
                         $('.%(menuid)s a').removeClass('%(cssclass)s');
                         $('.%(function)s').toggleClass('%(cssclass)s').css('background-position','%(cssposition)s')

             });
            </script>
            """ % dict(cssclass=cssclass,
                       menuid=menuid,
                       function=request.function,
                       cssposition=positions[request.function]
                       )

            return XML(jscript)
    else:
        return ''
