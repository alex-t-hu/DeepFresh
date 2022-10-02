// Copyright (c) 2020 Facebook, Inc. and its affiliates.
// All rights reserved.
//
// This source code is licensed under the BSD-style license found in the
// LICENSE file in the root directory of this source tree.

import UIKit

class ViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate{
    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var btnRun: UIButton!

    private var image : UIImage?
    private var inferencer = ObjectDetector()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        image = UIImage(named: "logo")!
        if let iv = imageView {
            iv.image = image
            btnRun.setTitle("Detect", for: .normal)
        }
    }

    @IBAction func runTapped(_ sender: Any) {
        btnRun.isEnabled = false
        btnRun.setTitle("Running ...", for: .normal)
        let resizedImage = image!.resized(to: CGSize(width: CGFloat(PrePostProcessor.inputWidth), height: CGFloat(PrePostProcessor.inputHeight)))
        print("line 29")
        let imgScaleX = Double(image!.size.width / CGFloat(PrePostProcessor.inputWidth));
        let imgScaleY = Double(image!.size.height / CGFloat(PrePostProcessor.inputHeight));
        print ("imgScaleX", imgScaleX)
    
        let ivScaleX : Double = (image!.size.width > image!.size.height ? Double(imageView.frame.size.width / image!.size.width) : Double(imageView.frame.size.height / image!.size.height))
        let ivScaleY : Double = (image!.size.height > image!.size.width ? Double(imageView.frame.size.height / image!.size.height) : Double(imageView.frame.size.width / image!.size.width))
        print("ivScaleX", ivScaleX)
        let startX = Double((imageView.frame.size.width - CGFloat(ivScaleX) * image!.size.width)/2)
        let startY = Double((imageView.frame.size.height -  CGFloat(ivScaleY) * image!.size.height)/2)
        print("startX", startX)
        guard var pixelBuffer = resizedImage.normalized() else {
            return
        }
        print("line 42")
        DispatchQueue.global().async {
            guard let outputs = self.inferencer.module.detect(image: &pixelBuffer) else {
                return
            }
            print("line 48")
            let nmsPredictions = PrePostProcessor.outputsToNMSPredictions(outputs: outputs, imgScaleX: imgScaleX, imgScaleY: imgScaleY, ivScaleX: ivScaleX, ivScaleY: ivScaleY, startX: startX, startY: startY)
            print("HERERERER")
            DispatchQueue.main.async {
                PrePostProcessor.showDetection(imageView: self.imageView, nmsPredictions: nmsPredictions, classes: self.inferencer.classes)
                self.btnRun.isEnabled = true
                self.btnRun.setTitle("Detect", for: .normal)
            }
        }
    }

    @IBAction func photosTapped(_ sender: Any) {
        PrePostProcessor.cleanDetection(imageView: imageView)
        let imagePickerController = UIImagePickerController()
        imagePickerController.delegate = self;
        imagePickerController.sourceType = .photoLibrary
        self.present(imagePickerController, animated: true, completion: nil)
    }
    
    @IBAction func cameraTapped(_ sender: Any) {
        PrePostProcessor.cleanDetection(imageView: imageView)
        if UIImagePickerController.isSourceTypeAvailable(.camera) {
            let imagePickerController = UIImagePickerController()
            imagePickerController.delegate = self;
            imagePickerController.sourceType = .camera
            self.present(imagePickerController, animated: true, completion: nil)
        }
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        image = info[UIImagePickerController.InfoKey.originalImage] as? UIImage
        image = image!.resized(to: CGSize(width: CGFloat(PrePostProcessor.inputWidth), height: CGFloat(PrePostProcessor.inputHeight)*image!.size.height/image!.size.width))
        imageView.image = image
        self.dismiss(animated: true, completion: nil)
    }
}


