import hardpotato as hp
import os
MODEL = "emstatpico"

if __name__ =="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)

    args = parser.parse_args()
    
    info = hp.potentiostat.Info(MODEL)
    info.specifications()
    hp.potentiostat.Setup(model=MODEL, path="", folder="data")

    if args.filename:
        print("filename:", args.filename)
        for cable in [0,1,2]:
            os.system(f'ampy --port /dev/ttyACM0 run ~/pico/channel{cable}.py')
            for channel in [0,1]:
                eis = hp.potentiostat.EIS(fileName=args.filename+f'_{cable}_{channel}', ch=channel)
                eis.run()
