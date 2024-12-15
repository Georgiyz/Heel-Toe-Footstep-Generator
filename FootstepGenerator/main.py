import audio_file_handler as afh
import os
import pygubu
import waveform_effects as we


class FootstepApplication:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file("ui/ui.ui")
        self.mainwindow = builder.get_object('mainwindow', master)

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def on_generate_btn_press(self, event=None):
        status_msg = self.builder.get_object("status_msg")
        status_msg.config(text="Generating")

        # os.remove("media/stitched_pairs/stitched_pair.wav")
        # os.remove("media/output/output.wav")

        afh.generate_heel_toe_file()

        if self.builder.get_variable("pitch_control_active").get() == 1:
            pitch_shift_amount = self.builder.get_variable("pitch_scale_var")
            print("Applied pitch shift" + str(pitch_shift_amount.get()))
            we.apply_pitch_shift(pitch_shift_amount.get())

        if self.builder.get_variable("low_pass_control_active").get() == 1:
            low_pass_amount = self.builder.get_variable("low_pass_var")
            print("Applied low pass" + str(low_pass_amount.get()))
            we.apply_low_pass_filter(low_pass_amount.get())
            # we.apply_low_pass_filter()

        if self.builder.get_variable("reverb_control_active").get() == 1:
            room_amount = self.builder.get_variable("room_size_var")
            print("Applied room reverb" + str(room_amount.get()))
            we.apply_reverb(room_amount.get())

        if self.builder.get_variable("gain_control_active").get() == 1:
            gain_amount = self.builder.get_variable("gain_var")
            print("Applied gain" + str(gain_amount.get()))
            we.apply_gain(gain_amount.get())

        we.apply_effects_chain()
        

def main():
    # create_application()
    # generate_footsteps()
    pass


def generate_footsteps():
    afh.generate_heel_toe_file()
    
    we.apply_pitch_shift()
    we.apply_low_pass_filter()
    we.apply_reverb()
    we.apply_effects_chain()

    
if __name__ == '__main__':
    # main()
    app = FootstepApplication()
    app.run()
