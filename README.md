# Vectors
* speed (aka movement) and position values use a Vector class
* MoveKey holds key configuration
* EventManager holds logic for event management (aka key pressed...)
* Entity holds Rect, parallax and movement logic
* protagonist can move in 2d and change parallax for a 3d effect.

# Next steps 
## Priority: High
* [x] Element display should be based on parallax. (near objects should draw on top of far objects)
* [x] Allow camera to change position
    * [x] allow camera x axis movement
    * [x] allow camera y axis movement
    * [x] allow camera parallax change
* [x] consider camera position change for element drawing
    * [x] deal with camera movement on the x axis
    * [x] deal with camera movement on the y axis
    * [x] deal with camera parallax change
* [ ] implement camera shake
    * [x] initial implementation -- working camera shake
    * [ ] assess if current way of going about implementation makes sens
    * [ ] cleanup implementation -- make the code resonably pretty
* [ ] have each Entity (Camera also) hold their own movement keys and movement logic

## Priority: Low (aka when/if I feel like it)
- [ ] Camera changes
    - [ ] do not draw elements that have a parallax higher than the camera (they are "behind" the camera)
    - [ ] allow camera to "switch" positional logic. Instead of following its own Rect, follow passed rect.
