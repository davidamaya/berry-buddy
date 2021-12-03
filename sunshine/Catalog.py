import tkinter as tk
from tkinter import Button
from tkinter import ttk
import sqlite3 as sl

berryNames = []

con = sl.connect("berries.db")

# with con:
#     con.execute("""
#         CREATE TABLE BERRY (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             description TEXT
#         );
#     """)
#
# sql = 'INSERT INTO BERRY (id, name, description) values(?, ?, ?)'
# data = [
#     (1, 'Gooseberry', """Gooseberries are members of the Ribes genus and look very
#     similar to currants, though there are some important distinctions. They are both perennial
#     bushes with somewhat vining stalks that arise from the roots. When cut back or
#     burned back, the plant will send up many very straight stalks.
#     The stalks of the gooseberries are covered in spines. The fruits of goose-berry are
#     also covered in little spines. Currants, on the other hand, have no spines on the stalk
#     or fruit. But both plants have the very same growth patterns, and leaves that look
#     like a three-lobed mitten.
#
#     Habitats: Mountains, in chaparral, on flat plains, along rivers.
#
#     Range: Common locally.
#
#     Tools: No special tools needed to harvest, though gloves are recommended.
#
#     """),
#     (2, 'Coffeeberry', """California coffeeberry is a member of the Buckthorn family
#     (Rhamnaceae). There are fifty to fifty-two genera of the
#     Buckthorn family worldwide, with about 950 species.
#     There are fifty species of the Frangula genus, with three
#     species found in California. Aside from the two species listed
#     above, there is Frangula rubra, or Sierra coffeeberry.
#     Description: F. californica and its six subspecies are most
#     common in Southern California; F. purshiana and its three
#     subspecies are found more commonly in the northern part of
#     California. These are small shrubs to large trees, depending on
#     location and species. F. californica is typically no more than
#     8 feet tall, whereas F. purshiana is significantly taller, very
#     treelike. The leaves are alternately arranged, an inch or two
#     in length, typically bright green, narrowly oblong, with tiny
#     teeth on the margins.
#
#     Uses: Seeds are used for a beverage and bark is used for a laxative.
#
#     Habitats: Scattered widely in chaparral and woodland but generally closer to the coast.
#
#     Tools: No special tools needed to collect fruits.
#     """),
#     (3, 'Elderberry', """The elderberry is a member of the Muskroot family(Adoxaceae).
#     This family has five genera and about 200
#     species worldwide. Only two of the genera are represented
#     in California, one of which is Sambucus. There are twenty
#     species of Sambucus worldwide, and according to the
#     latest classification, you'll find four types of elderberries in
#     California:
#
#     •S. nigra, subspecies caerulea (Mexican elder or blue elderberry), found at lower
#     elevations, throughout the chaparral. The fruit is nearly black when ripe, with a
#     white glaucous coating making it appear blue.
#     •S. racemosa, which has red or purplish-black fruits
#     •S. racemosa var. melanocarpa (black elderberry), found at higher locations and
#     having purplish-black fruits
#     • S. racemosa var. racemosa (red elderberry), having red fruits, and preferring moist
#     areas
#
#     Uses: Flowers are used for tea and food; berries for "raisins," jam, jelly, and juice.
#
#     Habitats: Chaparral, mountains, desert, urban fringes, and generally in most
#     environments.
#
#     Range: Throughout California.
#
#     Tools: Snippers and bags.
#
#     """),
#     (4, 'Wild Grape', """Native wild grapes belong to the Grape family (Vitaceae). The
#     Grape family has about fifteen genera and about 800 species
#     worldwide. In California, this family is represented by only
#     two genera, Parthenocissus (the Virginia creeper) and Vitis
#     (grapes). Though there are sixty-five known species of Vitis, it
#     is only represented in California by three species, one of which
#     is the introduced cultivated grape (V. vinifera). The other two
#     are the California wild grape (V. californica) and the desert
#     wild grape (V. girdiana).
#
#     Uses: Fruits are eaten raw or cooked and the leaves are used in Middle Eastern cooking.
#
#     Habitats: Prefers riparian areas and moist, shady canyons.
#
#     Range: Widespread in localized areas.
#
#     Tools: Clippers and bags.
#
#     """),
#     (5, 'Cherry', """Wild cherries are members of the Rose family (Rosaceae),
#     which contains 110 genera and 3,000 species worldwide.
#     Species from forty-five of the genera are found in California.
#
#     The four wild cherries in California are:
#     • Hollyleaf cherry (Prunus ilicifolia, subspecies ilicifolia)
#     • Catalina Island cherry (Prunus ilicifolia, subspecies lyonii)
#     •Bitter cherry (P. emarginata)
#     • Western chokecherry (P. virginiana var. demissa)
#
#     The first two wild cherries listed above are evergreen trees or bushes in
#     California. The leaves are stiff and shiny, with teeth on the margins (depending on
#     species). Bitter cherry and western chokecherry are deciduous.
#     One way to identify the plant is to crush the leaves, wait a few seconds, and
#     then smell them. They will have a distinct aroma of bitter almond extract, your
#     clue that the leaf contains cyanide (hydrocyanic acid). The fruits are very much like
#     cultivated cherries, except the color is darker red, almost maroon, sometimes even
#     darker. The flesh layer can be very thin in dry years, and thicker in the seasons
#     following a good rain. Like domestic cherries, there is a thin shell around the meaty
#     inside of the seed.
#
#     Uses: The flesh of the fruit is used in jams and jellies, and even cough syrup; the
#     meat of the large seed can be processed into a flour.
#
#     Habitats: Chaparral, coastal ranges, riparian zones, urban fringes.
#
#     Range: Wild cherries can be found widely throughout the state, often growing in
#     urban vacant lots and hedgerows.
#
#     Tools: You don't need any special tools to collect cherries, just a bag or box.
#
#     """),
#     (6, 'Currant', """Currants are members of the Ribes genus and look very
#     similar to gooseberries. They are both perennial
#     bushes with somewhat vining stalks that arise from the roots. When cut back or
#     burned back, the plant will send up many very straight stalks.
#     The stalks of the gooseberries are covered in spines. The fruits of goose-berry are
#     also covered in little spines. Currants, on the other hand, have no spines on the stalk
#     or fruit. But both plants have the very same growth patterns, and leaves that look
#     like a three-lobed mitten.
#
#     Habitats: Mountains, in chaparral, on flat plains, along rivers.
#
#     Range: Common locally.
#
#     Tools: No special tools needed to harvest, though gloves are recommended.
#
#     """),
#     (7, 'Ground Cherry', """Ground cherry is a member of the Nightshade family
#     (Solanaceae), which consists of at least seventy-five genera
#     and about 3,000 species worldwide. Physalis is one of the
#     thirteen genera of the Nightshade family found in California.
#     Physalis contains about eighty-five species worldwide, with
#     seven species (not including varieties) found in California,
#     four of which are native.
#
#     This is an obvious nightshade plant when you see it. Ground cherry
#     is a low, sometimes sprawling plant that grows to about a foot tall, maybe taller in
#     certain circumstances. The leaves are typical lanceolate to ovate, often toothed. The
#     five-petaled flowers are usually yellow, but sometimes purple. The most obvious
#     feature of the ground cherry fruit is its enclosure in a papery sheath, giving it one of
#     its common names, husk tomato.
#
#     Uses: The fruits are eaten when they mature, and are fully ripe in the fall.
#     Otherwise, they must be cooked.
#
#     Habitats: The native species can be found in desert washes, slopes, rocky flats, etc.
#
#     Range: Desert regions.
#
#     Tools: Bag for collecting.
#
#     """),
#     (8, 'Huckleberry', """Huckleberry is a member of the Heath family (Ericaceae).
#     This family contains about one hundred genera and 3,000
#     species worldwide. In California, there are twenty-six genera.
#     The Vaccinium genus includes more than 400 species in the
#     world, with eight in California. In general, Vaccinium are
#     referred to as huckleberries, blueberries, cranberries, and even
#     bilberries, depending on the species. All are native, except V.
#     macrocarpon, which is the common cranberry.
#
#     These shrubs have alternate evergreen or deciduous leaves, which are
#     broadly lance-shaped. The stems are trailing to erect. The flower's petals generally
#     number four to five, with a corolla that is cup- or urn-shaped. The fruit could be red
#     or blue, large or small, and have flattened ends. Generally, the plants with the most
#     desirable fruits are the smaller shrubs, about 3 feet tall, with larger, sweet, juicy blue
#     berries measuring about ¼-to ½-inch in diameter.
#
#     Uses: The fruits are edible.
#
#     Habitats: Found in the woods, usually coniferous woods, in clearings, moist areas,
#     and shaded areas.
#
#     Range: The Vacciniums are forest inhabitants, mostly found in the northern half of
#     the state and into the Northwest.
#
#     Tools: A basket.
#
#     """),
#     (9, 'Juniper', """Juniper is a member of the Cypress family (Cupressaceae),
#     which has thirty genera and more than 130 species worldwide. Only seven genera
#     are found in California.There are about sixty-seven species of Junipers in the
#     Northern Hemisphere. In California, we have just five species of juniper, all
#      of which are considered native, including the Utah juniper V. osteosperma).
#
#      Junipers are shrubs or small trees with thin peeling bark. The leaves
#     are scalelike. The seed cone is 5 to 18 millimeters long, more or less round, fleshy
#     and berrylike, and a shade of blue that matures to brown. The aroma of the cones
#     has been described as ginlike.
#
#     Sometimes junipers are confused with cypress, but the cypress have larger,
#     harder cones with angular edges.
#
#     Uses: The berries are used for food and medicine.
#
#     Habitats: Dry slopes, pinyon woodlands, flats, sagebrush areas.
#
#     Range: More common in southern California, and found south into Baja California,
#     Arizona, and other adjacent states.
#
#     Tools: A bag or basket for collecting.
#
#      """),
#     (10, 'Nightshade',  """ The four related species of nightshade are members of the
#     Nightshade family (Solanaceae). There are seventy-five genera in the Night-shade
#     family, and 3,000 species worldwide. Eleven genera--one of which is Solanum- are
#     found in California. There are approximately 1,500 species of Solanum in the world,
#     with eighteen found in California. Many are toxic, and many are good foods.
#     Description: S. americanum (aka S. nodiflorum), S. douglasit, and S. xanti are native
#     nightshades; S. nigrum is not. S. americanum and S. nigrum are very similar
#     and sometimes difficult to distinguish from one another. The very young plant
#     resembles lambsquarters, except that the nightshade doesn't have an erect stem.
#     Rather, it's more widely branched. Also, though the individual leaves of both
#     nightshade and lambsquarters are quite similar, the nightshade lacks the mealy
#     coating of the lambsquarters', and lacks the often noticeable red in the axil of
#     the leaf, which is common in lambsquarters. The five-petaled white to lavender
#     flower is a very typical Nightshade family flower, resembling the flowers of garden
#     tomatoes. The fruits begin as tiny BB-size green fruits, and by August ripen into
#     purplish-black little "tomatoes." We've eaten all of the four listed Solanums with no
#     problems.
#
#     Uses: Fruits are used when ripe, either raw or cooked. Green fruits can be used
#     if cooked (fried or boiled). The young leaves are boiled and eaten by people from
#     Mexico (where it is somewhat popular and called '"yerba mora"), the Philippines, and
#     Hong Kong.
#
#     Cautions: Is it possible to confuse these nightshades with toxic species? According
#     to many, the species we've listed are toxic species, meaning don't eat the green,
#     raw fruits, and don't eat the leaves raw. Sickness is likely in either case. There are
#     individuals who experience sickness when they eat any member of the Night-shade
#     family, including eggplants, tomatoes, peppers, potatoes, etc.
#
#     Habitats: Common and widespread in chaparral areas, disturbed urban soils, and
#     wild areas on the fringe of urban areas.
#
#     Range: Widespread throughout much of the state.
#
#     Tools: No special tools are required.
#
#     """),
#     (11, 'Blackberry and Raspberry', """Blackberries and raspberries are members of the Rose family
#     (Rosacea). The Rose family contains 110 genera and 3,000
#     species worldwide. Species from forty-five of the genera are
#     found in California. Raspberries belong to the Rubus genus,
#     and there are 400 to 750 species of Rubus worldwide. There are
#     eleven species of Rubus in California (not including varieties).
#
#     The leaves of blackberries and raspberries are palmately divided (like
#     a hand) into three, five, or seven segments. The vines are twining on the ground or
#     over low hedges, and are characterized by their thorns, which makes it difficult to
#     wade too deep into any of the old hedgelike stands of wild blackberries. The flowers
#     are white and five-petaled, and are followed by the fruits, which are aggregate fruits.
#     Most people instantly recognize the shape of the blackberry because they've seen it
#     in the supermarket or in the backyard garden. The aggregate fruit is a collection of
#     sweet drupelets, with the fruit separating from the flower stalk to form a somewhat
#     hollow, thimblelike shape.
#
#     Uses: The ripe fruits are eaten fresh, or made into a variety of jams, jellies, and
#     juices. The leaves are sometimes used medicinally. Made into an infusion, the leaf
#     tea can be used to treat cases of mild diarrhea. Gargling with an infusion of
#     blackberry leaf is also good for mouth irritations, such as bleeding gums or sore
#     throat.
#
#     Habitats: The Rubus species and their kin are fairly widespread and distributed
#     throughout the state. These vines are at home growing in high elevations, in
#     chaparral, along dusty trails, along streams, near the beach .. everywhere!
#
#     Range: Blackberries and raspberries prefer areas where sufficient water is supplied.
#     They have also been widely planted, and survive well in diverse places.
#
#     Tools: Gloves and clippers can be a good idea when harvesting ripe blackberries. You
#     should also bring shallow baskets that can be stacked, so that the fragile fruits do
#     not get crushed.
#     """),
#     (12, 'Serviceberry', """Serviceberry is a large shrub or small tree with
#     deciduous leaves, often forming in dense thickets. The twigs
#     of this native are glabrous, and the leaf is elliptical to round,
#     with obvious serrations, generally serrated above the middle
#     of the leaf. The flowers are five-petaled, white, fragrant, in
#     clusters of a few to many. The fruit is a pome of two
#     to five papery segments, berrylike, generally spherical, and
#     bluish black in color.
#
#     Uses: Berries are edible.
#
#     Habitats: Found in red fir forests and lodgepole pine forests, up to about the 7,000
#     foot level and occasionally in wetlands. Also found in open areas.
#
#     Range: Serviceberries are found in the northern two-thirds of the state.
#
#     Tools: A basket for collecting.
#
#     """),
#     (13, 'Strawberry', """The leaves are all basal, generally three-lobed,
#     with each leaflet having fine teeth. It looks just the strawberry
#     you grow in your garden, but smaller.
#     Technically, the strawberry is an aggregate accessory fruit,
#     meaning that the fleshy part is derived not from the plant's
#     ovaries, but from the receptacle that holds the ovaries. In
#     other words, what we call "the fruit" (because duh!, it looks
#     like a fruit) is the receptacle, and all the little seeds on the
#     outside of the "fruit" are technically referred to as achenes,
#     actually one of the ovaries of the flower with a seed inside it.
#
#     Uses: The fruits are eaten.
#
#     Habitats: Wild strawberry prefers higher elevation forests and clearings.
#
#     Range: Found widely throughout the state, though more common in the northern
#     California.
#
#     Tools: Basket.
#
#     """),
#     (14, 'Toyon', """Toyon can grow to be a medium-size tree, and
#     is probably most conspicuous in the winter when it's covered
#     with clusters of orange-red fruits. The tree is found in the
#     chaparral zones, and often planted on the fringes of the
#     urban areas. The leaves are leathery and ovate, with toothed
#     margins. The tree is evergreen and can be a large bush or a
#     small tree. Each flower, which forms in the summer, is white
#     and five-petaled, about ¼ inch wide. The clusters of orange-
#     red fruit ripen from about November into January.
#
#     Uses: Berries are cooked, dried, or made into flour.
#
#     Habitats: Chaparral hillsides, canyons, and slopes; sometimes cultivated.
#
#     Range: Found throughout the state, mostly in the western half.
#
#     Tools: Just a bag for collecting the berries.
#
#     """)
# ]
#
# with con:
#     con.executemany(sql, data)

with con:
    data = con.execute("SELECT * FROM BERRY")
    result = data.fetchall()
    for row in result:
        berryNames.append(row[1])


class Catalog(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#e2c7d8")
        self.controller = controller

        # label_frame = tk.Frame(self,bg="#95658B")
        # label_frame.pack(fill='both',expand=True)

        # Put your code here with label_frame. Take test 1 out
        label = ttk.Label(self, text="Berry Buddy Catalog", font=('Helvetica', 30))
        label2 = ttk.Label(self, text="")
        label3 = ttk.Label(self, text="")
        button2 = tk.Button(self, text="Close", command=lambda: resetLabelText())

        label.pack(pady=10)

        # # Created entry box
        myEntry = tk.Entry(self, font=('Helvetica', 20))
        myEntry.pack()
        #
        # # Create a list box
        myList = tk.Listbox(self, width=50)
        myList.pack()

        # # Update the listbox
        def update(data):
            # Clear the listbox so it can reset each time a new berry is entered
            myList.delete("0", "end")
            # Add berries top listbox
            # enumerate allows us to get the index
            # loop goes through the list of berries in the box
            for i, item in enumerate(data):
                # i is the index and item is the berry itself
                myList.insert(i, item)

        # Update entry box with listbox clicked
        def fillout(event):
            # Deletes anything in the entry box
            myEntry.delete(0, "end")

            # Add clicked list item to entry box
            myEntry.insert(0, myList.get("anchor"))
            global BERRY_NAME
            BERRY_NAME = myEntry.get()
            if BERRY_NAME in berryNames:
                with con:
                    data = con.execute(f"SELECT * FROM BERRY WHERE name == '{myEntry.get()}'")
                    result = data.fetchone()
                    if result:
                        label2.pack(pady=20)
                        label2.config(text=result[1], font=('Helvetica', 30))
                        label3.config(text=result[2])
                        label3.pack(pady=20)
                        button2.pack(side=tk.BOTTOM)

        # # Create function to check entry vs listbox
        def check(event):
            # Grab what was typed
            typed = myEntry.get()
            if typed == '':
                # The berryNames list will show up if there is nothing in the search bar
                data = berryNames
            else:
                data = []
                for item in berryNames:
                    if typed.lower() in item.lower():
                        data.append(item)

            # Updates our listbox with selected items
            update(data)

        #
        # # Add berryNames to list
        update(berryNames)
        #
        # # Create a binding on the listbox onclick... predicts entry based on what is in the listbox
        myList.bind('<<ListboxSelect>>', fillout)
        #
        # # Create a binding on the entry box
        myEntry.bind('<KeyRelease>', check)

        def resetLabelText():
            label2.config(text='')
            label3.config(text='')
            myEntry.delete("0", "end")

        button_frame = tk.Frame(self, bg="#95658B")
        button_frame.pack(fill='both', expand=True)

        def back():
            resetLabelText()
            controller.show_frame('PageOne')

        home_button = tk.Button(button_frame, text='Home', command=back, highlightbackground="#e2c7d8",
                                foreground="black")

        button1 = Button(button_frame, text="Homepage", width=8,
                         highlightbackground="pink", foreground="black", command=back)
        home_button.grid(row=2, column=6, sticky=tk.S)
        button_frame.place(relx=1, rely=1, anchor=tk.SE)

# Sunshine's Code End

