

#Load the image as a nibabel Image

#Read in the image data

#Slice image data into frames along a dimension

#Apply any transforms to the data (.resize((128,128), Image.ANTIALIAS)) (in PIL)

#Transform the slices to grayscale (0 to 255) (in PIL)

#Write each slice to a jpeg (from PIL)

#Create a gif from the jpegs (with imageio)


>>> images = []
>>>
>>> for filename in all_files:
...     images.append(imageio.imread(filename))
...
>>> output_file = 'test_gif.gif'
>>> imageio.mimsave(output_file, images, duration=0.5)



img = nib.load(imagefile)

img.get_data()
img.get_affine()

# determine slice index
    ndim = im_read.shape
    if len(ndim) != 4:
        err = 'Expected 4D volume, got {} dimensions'
        err = err.format(len(ndim))
        raise ValueError(err)

    msg = 'Volume Dimensions: {}'
    msg = msg.format('x'.join(str(n) for n in ndim))
    logger.info(msg)

    msg = 'Time dimension is {} with {} frames'
    msg = msg.format(time_axis, ndim[time_axis])
    logger.info(msg)

    msg = 'Slice dimension is {} with {} slices'
    msg = msg.format(slice_axis, ndim[slice_axis])
    logger.info(msg)

    msg = 'Image frames are {}'
    msg = msg.format('x'.join(str(n) for i, n in enumerate(ndim)
                              if i not in (time_axis, slice_axis)))
    logger.info(msg)

# Dump the frames to jpg files
    transforms = [
        lambda im: im.resize((128, 128), Image.ANTIALIAS),
        lambda im: im.rotate(GIF_ROTATION),
    ]
    images = transform_frames(
        data=im_read,
        time_axis=time_axis,
        slice_axis=slice_axis,
        transforms=transforms,
        dist=GIF_DISTANCE,
    )

    if output_prefix in (0, None, ''):
        output_prefix = fix_output_prefix(input_img)
        output_dir = input_dir
    else:
        output_prefix = os.path.realpath(output_prefix)
        output_dir = os.path.dirname(output_prefix)

    # create a temporary directory
    with mktempdir(dir=output_dir) as tempdir:

        pic_prefix = os.path.basename(output_prefix)
        pic_prefix = os.path.join(tempdir, pic_prefix)

        # Dump the frames to jpg files
        save_frames(images, prefix=pic_prefix, ext=pic_format)

        image_pattern = '{}*.{}'.format(pic_prefix, pic_format)
        image_pattern = os.path.join(tempdir, image_pattern)

        # convert to gif by ImageMagick
        outfile = output_prefix + '.gif'
        cmd = ['gm', 'convert',
               '-delay', '8',
               '-loop', '0',
               image_pattern,
               outfile]
        logger.debug('Calling: {}'.format(cmd))
        subprocess.check_call(' '.join(cmd), shell=True)

    if not os.path.isfile(outfile):
        err = 'Failed to produce gif: "{}"'
        err = err.format(outfile)
        logger.error(err)
        raise RuntimeError(err)
    return outfile