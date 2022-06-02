# Question: Cyber Warriors 1:
    What date was this issue published? (flag ctf{MM-DD-YYYY})
*ctf{08-21-1995}*

## Writeup:
Using the text of the cover, a quick google search presents the exact issue via Time's archives. 


# Question: Inside the Cyber Warrior #2
    Highlighted in this issue, was a movie. How many theaters showed this movie as a part of its opening?
*ctf{1591}*

## Writeup:
Digging further into the Time Official Archive site for this issue, you see:
 -> Inside this Issue
        -> Arts & Entertainment Section
                -> Article on [Babe](http://content.time.com/time/magazine/article/0,9171,983330,00.html) 
                    -> a Google search of "Babe" and box office information would return the number of 1591. 


# Question: Ode to Ye Olde Cougar Net:
    Use the attached photo and identify which entrance to a building on campus this is!

    Flag: ctf{building_direction}, for example: ctf{crabtree_east} . It is case insensitive.

    (Fun fact! There is no door on the east side of the Crabtree building)

*ctf{wilkinson_north}*

## Writeup:
Visible in the picture are three elements that can be used to quickly narrow down entrances on campus. These include:
- Number of Doors (3)
    - There exists a handful of double entrances with three doors wide, this narrows the list to a possible four or five.
- Pattern of Bricks in reflection/Cement Wall in reflection
    - The pattern of pavers is visible in the reflection, unique to the walk into the Wilkinson center. 
    - The cement wall is also very unique to the wilkinson entrance. 
- Internal flooring 
    - The tile within the entrence can be used to identify the building. 


# Question: Oh the roads you'll go:
    Can you imagine provo drivers in this intersection? I can't. Thank goodness it is x amount of miles from the crabtree. 

    Flag is : ctf{x} where x is the number of miles as the crow flies from the crabtree building to this intersection, within +/- 2 miles. 

*ctf{2088-92}*

## Writeup:
The following link was used in the final calculations. Identifying information include the two uncovered roadsigns, combined with the van in the foreground. The van indicates the picture was taken in boston someplace, and by aligning the two state route signs and the general intersection shape results in enough clues to make a guess within the mileage allowance. 

    https://www.google.com/maps/place/Crabtree+Technology+Building+-+CTB/@42.407864,-71.089404,16z/data=!4m5!3m4!1s0x874d90b76112313b:0x74bb149d78314b13!8m2!3d40.247761!4d-111.646828


# Question: Killer view eh?
    Can you identify this cool city caught from above?

    Flag format - `ctf{cityname}` (case insensitive)

*ctf{brasilia}*

## Writeup:
This one was more guesswork than anything. The city of Brasilia is famous for its deliberate arrangement of the city in the shape of a bird or an airplane. Any search with the words "city shaped like plane/bird" would have resulted in Brasilia showing up. Other points of reference, the picture was taken by Ian Cook, who only traveled to Ohio, DC and Brazil over the past year. As the picture is clearly taken from within an airplane, one could attempt to guess major cities along those flight paths. 


# Question: Dang BYU Parking.
    Finding parking on campus is the worst. It is however, a good skill to have at BYU. This picture was taken somewhere on campus, with parking nearby! Believe it or not! Can you identify which group owns the nearest parking spot to this photo?

    flag is: ctf{word_of_word/word}
*ctf{department_of_physics/astro}*

## Writeup: 

Given the hints, the spot needed to be near some parking and featured distinct tree/flower pots. By scanning campus via google maps, one can identify two or three locations on campus with these features. A well placed google streetview cursor places the desired parking spot within view. 
https://map.byu.edu/
https://www.google.com/maps/@40.2470061,-111.6497795,3a,15y,67.87h,80.61t/data=!3m6!1e1!3m4!1siEInEz3lVgOUUf9cL8vTNg!2e0!7i13312!8i6656