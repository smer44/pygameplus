#tutorial from https://www.youtube.com/watch?v=LFbePt8i0DI

import pygame
import sys
import array
import moderngl
#pip3 install moderngl

pygame.init()

screen = pygame.display.set_mode((800,600), pygame.OPENGL | pygame.DOUBLEBUF)
display = pygame.Surface((800,600))
clock = pygame.time.Clock()

img = pygame.image.load("../tests/mc_descengind_staircase.png")

ctx = moderngl.create_context()

#coordinates conversion
#coords in opengl -> from -1 to 0
data = [
    # position x,y, uv coords x,y
    -1.0,1.0,0.0,0.0, # topleft
    1.0,1.0,1.0,0.0, # topright
    -1.0,-1.0,0.0,1.0, #bottomleft
    1.0,-1.0,1.0,1.0, # bottomright
]# position x,y, uv coords x,y

quad_buffer = ctx.buffer(data=array.array("f",data))

#in input
#vec2 vert, 2 floats


vert_shader = '''
#version 330 core

in vec2 vert;
in vec2 texcoord;
out vec2 uvs;

void main(){
    uvs = texcoord;
    gl_Position = vec4(vert, 0.0,1.0);
    
    

}
'''

frag_shader = '''
#version 330 core

uniform sampler2D tex;
uniform float time;

in vec2 uvs;
out vec4 f_color;

void main(){
    //chanve uf here for displace 
    
    float timescale = sin(time * 0.05);
    vec2 timeuv = vec2(sin(uvs.x*2 + time * 0.05),cos(uvs.y*2 + time * 0.05));
    vec4 input_color =  texture(tex,uvs + timeuv * 0.1);
    vec2 add_color = (timeuv + input_color.rg)/2;
    
    f_color = vec4(add_color,0.5 + timescale, input_color.a);

}

'''

program = ctx.program(vertex_shader=vert_shader,fragment_shader=frag_shader)
render_object = ctx.vertex_array(program, [(quad_buffer,"2f 2f" , "vert", "texcoord")])


def surface_to_texture(surface):
    tex = ctx.texture(surface.get_size(),4)
    tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
    tex.swizzle = "BGRA"
    tex.write(surface.get_view("1"))
    return tex


t = 0
loop = True
while loop:
    t+=1
    display.fill((0,0,0))
    display.blit(img,pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    frame_tex = surface_to_texture(display)
    frame_tex.use(0)
    program['tex'] = 0
    program['time'] = t
    render_object.render(mode = moderngl.TRIANGLE_STRIP)

    pygame.display.flip()

    frame_tex.release()
    clock.tick(60)




pygame.quit()

