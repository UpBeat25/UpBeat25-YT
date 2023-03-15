from array import array
import pygame
import moderngl

pygame.init()

# screen = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
class Shader:
    def __init__(self, a: int=1):
        super().__init__()
        self.ctx = moderngl.create_context()
        self.quad_buffer = self.ctx.buffer(data=array('f', [
        # position (x, y), uv coords (x, y)
        -1.0, 1.0, 0.0, 0.0,  # topleft
        1.0, 1.0, 1.0, 0.0,  # topright
        -1.0, -1.0, 0.0, 1.0,  # bottomleft
        1.0, -1.0, 1.0, 1.0,  # bottomright
    ]))
        self.vert_shader = '''
    #version 330 core
    
    in vec2 vert;
    in vec2 texcoord;
    out vec2 uvs;
    
    void main() {
        uvs = texcoord;
        gl_Position = vec4(vert, 0.0, 1.0);
    }
    '''
        self.frag_shader = '''
    #version 330 core
    
    uniform sampler2D tex;
    uniform float time;
    
    in vec2 uvs;
    out vec4 f_color;
    
    void main() {
        vec2 sample_pos = vec2(uvs.x, uvs.y);
        f_color = vec4(texture(tex, sample_pos).rg, texture(tex, sample_pos).b * %a, 1.0);
    }
    ''' % a
        self.program = self.ctx.program(vertex_shader=self.vert_shader, fragment_shader=self.frag_shader)
        self.render_object = self.ctx.vertex_array(self.program, [(self.quad_buffer, '2f 2f', 'vert', 'texcoord')])


    def surf_to_texture(self, surf):
        tex = self.ctx.texture(surf.get_size(), 4)
        tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
        tex.swizzle = 'BGRA'
        tex.write(surf.get_view('1'))
        return tex

    def shader(self, screen):
        frame_tex = self.surf_to_texture(screen)
        frame_tex.use(0)
        self.program['tex'] = 0
        self.render_object.render(mode=moderngl.TRIANGLE_STRIP)
        frame_tex.release()
