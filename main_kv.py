#:kivy 1.8.0

#:set maxtop 50
#:set labelh 25
#:set fontsize 30
#:set nrows 2

<MainMap>:
    mapview: mymap
    textinput: name

    canvas:
        Color:
            rgba: .2, .4, .6, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        font_size: fontsize
        center_x: root.width / 4
        top: root.top - maxtop / 2
        text: str(root.latitude)
        height: labelh

    Label:
        font_size: fontsize
        center_x: root.width * 3 / 4
        top: root.top - maxtop / 2
        text: str(root.longitude)
        height: labelh

    MapView:
        id: mymap
        zoom: self.map_source.get_max_zoom() - 3
        width: root.width
        height: root.height - drop.height * (nrows + 1)
        center_y: (nrows*drop.height + 2) + self.height / 2

    Button:
        id: drop
        text: 'Drop'
        height: 1.5 * maxtop
        width: root.width / 2
        center_x: self.width / 2
        center_y: self.height / 2
        on_press: root.drop()

    Button:
        id: reset
        text: 'Reset'
        height: 1.5 * maxtop
        width: root.width / 2
        center_x: drop.width + self.width / 2
        center_y: drop.center_y
        on_press: root.reset()

    Button:
        id: save
        text: 'Save'
        height: 1.5 * maxtop
        width: root.width / 2
        center_x: drop.center_x
        center_y: drop.center_y * 3
        on_press: root.save()

    TextInput:
        id: name
        text: "node" + str(root.nodesnum)
        multiline: False
        height: 1.5 * maxtop
        width: root.width / 2
        center_x: root.width * 3 / 4
        center_y: save.center_y